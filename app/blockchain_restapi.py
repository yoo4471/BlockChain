from flask import render_template, flash, redirect, request, Response
from app import app
import json, requests

blockchain_ibm = 'https://d8ab2f755f2d4f38a76ceff057b45bf0-vp0.us.blockchain.ibm.com:5003'
enrollId = 'user_type1_0'
enrollSecret='f473edeb49'
chaincodeID_name=""
secureContext = ""

def login():
    try:
        url = blockchain_ibm + '/registrar'
        payload = {
    	  'enrollId': enrollId,
    	  'enrollSecret': enrollSecret
    	}
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        return r.text
    except:
        return "Chaincode is not working."

#DEPLOY
@app.route('/init', methods=['GET'])
def init():
    url = blockchain_ibm + '/chaincode'
    payload = {
          "jsonrpc": "2.0",
          "method": "deploy",
          "params": {
            "type": 1,
            "chaincodeID":{
                "name": "mycc"
            },
            "ctorMsg": {
                "args":[""]
            },
            "secureContext": "admin"
          },
          "id": 1
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    js = json.loads(r.text)
    js = json.dumps(js)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

#INVOKE
@app.route('/user_insert', methods=['GET'])
def user_insert(userID, password):
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name":"mycc"
          },
          "ctorMsg": {
             "args":["user_insert", userID, password]
          },
          "secureContext": "admin"
      },
      "id": 3
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    js = json.loads(r.text)
    js = json.dumps(js)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

#INVOKE
@app.route('/home_insert', methods=['GET'])
def home_insert(userID, citycode, address, hometype, room, area, elevator, parking):
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name":"mycc"
          },
          "ctorMsg": {
             "args":["home_insert", userID, citycode, address, hometype, room, area, elevator, parking]
          },
          "secureContext": "admin"
      },
      "id": 3
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    js = json.loads(r.text)
    js = json.dumps(js)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

#INVOKE
@app.route('/pet_insert', methods=['GET'])
def pet_insert(userID, name, birth, gender, kind, size, ns, vac):
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name":"mycc"
          },
          "ctorMsg": {
             "args":["pet_insert", userID, name, birth, gender, kind, size, ns, vac]
          },
          "secureContext": "admin"
      },
      "id": 3
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    js = json.loads(r.text)
    js = json.dumps(js)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

#INVOKE
@app.route('/user_change', methods=['GET'])
def user_change(userID, newpassword, ap):
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name":"mycc"
          },
          "ctorMsg": {
             "args":["user_change", userID, newpassword, ap]
          },
          "secureContext": "admin"
      },
      "id": 3
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    js = json.loads(r.text)
    js = json.dumps(js)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

#INVOKE
@app.route('/pet_change', methods=['GET'])
def pet_change(userID, size, ns, vac):
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name":"mycc"
          },
          "ctorMsg": {
             "args":["pet_change", userID, size, ns, vac]
          },
          "secureContext": "admin"
      },
      "id": 3
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    js = json.loads(r.text)
    js = json.dumps(js)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

#INVOKE
@app.route('/home_delete', methods=['GET'])
def home_delete(userID):
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name":"mycc"
          },
          "ctorMsg": {
             "args":["home_delete", userID]
          },
          "secureContext": "admin"
      },
      "id": 3
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    js = json.loads(r.text)
    js = json.dumps(js)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

#INVOKE
@app.route('/pet_delete', methods=['GET'])
def pet_delete(userID):
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name":"mycc"
          },
          "ctorMsg": {
             "args":["pet_delete", userID]
          },
          "secureContext": "admin"
      },
      "id": 3
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    js = json.loads(r.text)
    js = json.dumps(js)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

#INVOKE
@app.route('/trade_insert', methods=['GET'])
def trade_insert(petsitterID, consumerID, ts, te, tc, ta, th):
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name":"mycc"
          },
          "ctorMsg": {
             "args":["trade_insert", petsitterID, consumerID, ts, te, tc, ta, th]
          },
          "secureContext": "admin"
      },
      "id": 3
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    js = json.loads(r.text)
    js = json.dumps(js)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

#Qeury
@app.route('/user_read', methods=['GET'])
def user_read(userID):
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "query",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name":"mycc"
          },
          "ctorMsg": {
             "args":["user_read",userID]
          },
          "secureContext": "admin"
      },
      "id": 3
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    js = json.loads(r.text)
    js = json.dumps(js)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

#Qeury
@app.route('/home_read', methods=['GET'])
def home_read(userID):
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "query",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name":"mycc"
          },
          "ctorMsg": {
             "args":["home_read",userID]
          },
          "secureContext": "admin"
      },
      "id": 3
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    js = json.loads(r.text)
    js = json.dumps(js)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

#Qeury
@app.route('/pet_read', methods=['GET'])
def pet_read(userID):
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "query",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name":"mycc"
          },
          "ctorMsg": {
             "args":["pet_read",userID]
          },
          "secureContext": "admin"
      },
      "id": 3
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    js = json.loads(r.text)
    js = json.dumps(js)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

#Qeury
@app.route('/city_search', methods=['GET'])
def city_search(citycode):
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "query",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name":"mycc"
          },
          "ctorMsg": {
             "args":["city_search", citycode]
          },
          "secureContext": "admin"
      },
      "id": 3
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    js = json.loads(r.text)
    js = json.dumps(js)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

#Qeury
@app.route('/trade_search', methods=['GET'])
def trade_search(petsitterID, consumerID, tc):
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "query",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name":"mycc"
          },
          "ctorMsg": {
             "args":["trade_search", petsitterID, consumerID, tc]
          },
          "secureContext": "admin"
      },
      "id": 3
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    js = json.loads(r.text)
    js = json.dumps(js)

    resp = Response(js, status=200, mimetype='application/json')
    return resp
