import json
import os

from flask import Flask
from flask import request
from flask import make_response

@app.route('/demo', methods=['GET'])
def demo_reply():
  return 'Hello there my friend!!'
  

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
