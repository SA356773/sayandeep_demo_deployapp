import json
import os

from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('/demo',methods=['GET'])
def demo():
  speech = 'Hello World'
  my_result =  {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-demo-webhook-sample"
    }
  res = json.dumps(my_result, indent=4)
  r = make_response(res)
  r.headers['Content-Type'] = 'application/json'
  return r
  
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
