from flask import Flask, abort, request 
import json

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def parse_json():
    try:
        string = request.json['string_to_cut']
    except:
        print('POST request key not recognized')
        abort(400)
    result_string = cut_string(string)
    return_json = {
        "return_string": result_string,
    }
    return json.dumps(return_json)

def cut_string(string):
    if len(string) > 1:
        return string[2::3]
    else:
        return ""

if __name__ == '__main__':
    app.run(debug = True)