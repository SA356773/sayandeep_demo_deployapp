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
    print(json.dumps(req, indent=4))
    res = createResponse(req)
    return res



def createResponse(req):
  result = req.get("queryResult")
  if result.get("action") == "input.unknown":
        print ("Failed to recognize!!..passing to the next engine")
        my_result = {
        "fulfillmentText": "Fallback intent",
        "source": "Demo-DialogFlow-Example"
        }
        res = json.dumps(my_result, indent=4)
        r = make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r

  if result.get("action") != "animal_info":
        return{}
  parameters = result.get("parameters")
  animal = parameters.get("AnimalEntity")
  speech = 'Hello,received response from the backend application, this is a demo joke on {}'.format(animal)
  print ("Voice output : "+speech)
  my_result = {
	 "fulfillmentText": speech,
     "source": "Demo-DialogFlow-Example"
  }
  res = json.dumps(my_result, indent=4)
  r = make_response(res)
  r.headers['Content-Type'] = 'application/json'
  return r
  
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='127.0.0.1', threaded=True)
