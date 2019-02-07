import json
import os

from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('/webhook',methods=['POST'])
def webhook():
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
  my_result = {
        "speech": speech,
        "displayText": speech,
        "source": "apiai-weather-webhook-sample"
  }
  res = json.dumps(my_result, indent=4)
  r = make_response(res)
  r.headers['Content-Type'] = 'application/json'
  return r
  
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
