#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "user.id":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    _id = parameters.get("user-id")
	_pass1 = parameters.get("password")

   
 cost = {'Suraj':111, 'Shubham':222, 'Ravi':333, 'Yash':444, 'Raju':555, 'Krishna':666, 'Ravibhushan':777}

  
if(str(cost[_id])==_pass1):
  speech = "Succesfull Login"
else:
 speech = "Wrong Credential"

  print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
