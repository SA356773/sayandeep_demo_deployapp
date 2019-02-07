import json
import os

from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('/demo',methods=['POST'])
def demo():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    # commented out by Naresh
    print(json.dumps(req, indent=4))

    res = createResponse(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r



def createResponse(req):
  if req.get("result").get("action") != "animal_info":
        return {}
  paramters = result.get("parameters")
  animal = parameters.get("AnimalEntity")
  speech = 'Hello, this is sa demo joke on {}'.format(animal)
  my_result =  {
  "conversationToken": "[]",
  "expectUserResponse": true,
  "expectedInputs": [
    {
      "inputPrompt": {
        "richInitialPrompt": {
          "items": [
            {
              "simpleResponse": {
                "textToSpeech": speech
              }
            }
          ]
        }
      },
      "possibleIntents": [
        {
          "intent": "assistant.intent.action.TEXT"
        }
      ],
      "speechBiasingHints": [
        "$AnimalEntity"
      ]
    }
  ],
  "responseMetadata": {
    "status": {
      "message": "Success (200)"
    },
    "queryMatchInfo": {
      "queryMatched": true,
      "intent": "b894ab2c-3e6f-4ad7-8860-5bc4c4e8727a"
    }
  }
}
  res = json.dumps(my_result, indent=4)
  r = make_response(res)
  r.headers['Content-Type'] = 'application/json'
  return r
  
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
