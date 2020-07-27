Techincal sample for Lyft Software Engineering Apprenticeship

Objective: If you don’t have a current code sample you can share, please write a small web application in one of the above languages (Python/Ruby/Node). It only needs to accept a POST request to the route “/test” which accepts one argument “string_to_cut” returns a JSON object with the key “return_string” and a string containing every third letter from the original string. E.g. if you POST {"string_to_cut": "iamyourlyftdriver"}, it will return: {"return_string": "muydv"}.]

Testing: To see expected behavior you can test against a current working example with the command: curl -X POST https://lyft-interview-test.herokuapp.com/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'

MUST INSTALL Flask before running this code: python3 -m pip install Flask

Running local server (replace python3 with whatever command you are using): python3 lyft.py

Command for testing on the local server: curl -X POST http://localhost:5000/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'