from flask import render_template, flash, redirect, request, Response
from app import app
import json, requests
from . import function


blockchain_ibm = 'https://4b469ea7ae5d4d3c8574f329e59a2d89-vp2.us.blockchain.ibm.com:5001'
chaincodeID_path = "https://github.com/liil93/last_chaincode"

enrollId = 'user_type1_0'
enrollSecret = '580029b4e5'
secureContext = enrollId

#login
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

#DEPLOY - init
def deploy():
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "deploy",
      "params": {
          "type": 1,
          "chaincodeID":{
              "path": chaincodeID_path
          },
          "ctorMsg": {
             "args": [""]
          },
          "secureContext": secureContext
      },
      "id": 0
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.text

#INVOKE - save_petsitter
def save_petsitter(arg):
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name": '0bca8c9a73db7f25cfbdb3893ec7950f766e06e89d6edb1e1a9a94f93e957d56453ab629e1d47ae13d13b13457ebe793d25b00c33a5f56075f25f217ea8567fd'
          },
          "ctorMsg": {
             "function": "save_petsitter",
             "args": [
                arg[0], arg[1], arg[2], arg[3], arg[4], arg[5], arg[6], arg[7], arg[8], arg[9], arg[10], arg[11], arg[12], arg[13]
             ]
          },
          "secureContext": secureContext
      },
      "id": 0
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.text

#INVOKE - modify_petsitter
def modify_petsitter():
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name": "14330cb9a135478b6e9facddb25c83f70567a0426d3a935f660eb15a448fe9e41fdb25172dd1fa20742bbedab06f0561dfa9a8d9d40369da1df74666ebacc74e"
          },
          "ctorMsg": {
             "function": "modify_petsitter",
             "args": [
                "userID", "sceretkey", "contact"
             ]
          },
          "secureContext": secureContext
      },
      "id": 0
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.text

#INVOKE - delete_petsitter
def delete_petsitter():
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name": "14330cb9a135478b6e9facddb25c83f70567a0426d3a935f660eb15a448fe9e41fdb25172dd1fa20742bbedab06f0561dfa9a8d9d40369da1df74666ebacc74e"
          },
          "ctorMsg": {
             "function": "delete_petsitter",
             "args": [
                "userID", "sceretkey", "type", "locate"
             ]
          },
          "secureContext": secureContext
      },
      "id": 0
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.text

#INVOKE - save_home_address
def save_home_address(arg):
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name": '0bca8c9a73db7f25cfbdb3893ec7950f766e06e89d6edb1e1a9a94f93e957d56453ab629e1d47ae13d13b13457ebe793d25b00c33a5f56075f25f217ea8567fd'
          },
          "ctorMsg": {
             "function": "save_home_address",
             "args": [
                arg[0], arg[1], arg[2], arg[3], arg[4], arg[5]
             ]
          },
          "secureContext": secureContext
      },
      "id": 0
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.text

#INVOKE - save_home_room
def save_home_room(arg):
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name": '0bca8c9a73db7f25cfbdb3893ec7950f766e06e89d6edb1e1a9a94f93e957d56453ab629e1d47ae13d13b13457ebe793d25b00c33a5f56075f25f217ea8567fd'
          },
          "ctorMsg": {
             "function": "save_home_room",
             "args": [
                arg[0], arg[1], arg[2]
             ]
          },
          "secureContext": secureContext
      },
      "id": 0
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.text

#INVOKE - save_home_car_elevator
def save_home_car_elevator(arg):
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name": '0bca8c9a73db7f25cfbdb3893ec7950f766e06e89d6edb1e1a9a94f93e957d56453ab629e1d47ae13d13b13457ebe793d25b00c33a5f56075f25f217ea8567fd'
          },
          "ctorMsg": {
             "function": "save_home_car_elevator",
             "args": [
                arg[0], arg[1], arg[2]
             ]
          },
          "secureContext": secureContext
      },
      "id": 0
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.text

#INVOKE - modify_home_address
def modify_home_address():
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name": function.Get_key()
          },
          "ctorMsg": {
             "function": "modify_home_address",
             "args": [
                "userID", "sceretkey"
             ]
          },
          "secureContext": secureContext
      },
      "id": 0
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.text

#INVOKE - modify_home_room
def modify_home_room():
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name": function.Get_key()
          },
          "ctorMsg": {
             "function": "modify_home_room",
             "args": [
                "userID", "sceretkey"
             ]
          },
          "secureContext": secureContext
      },
      "id": 0
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.text

#INVOKE - modify_home_car_elevator
def modify_home_car_elevator():
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name": function.Get_key()
          },
          "ctorMsg": {
             "function": "modify_home_car_elevator",
             "args": [
                "userID", "sceretkey"
             ]
          },
          "secureContext": secureContext
      },
      "id": 0
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.text

#INVOKE - save_tran
def save_tran():
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name": function.Get_key()
          },
          "ctorMsg": {
             "function": "save_tran",
             "args": [
                "userID", "sceretkey"
             ]
          },
          "secureContext": secureContext
      },
      "id": 0
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.text

#Query - read_petsitter
def read_petsitter():
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "query",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name": function.Get_key()
          },
          "ctorMsg": {
             "function": "read_petsitter",
             "args": [
                "userID"
             ]
          },
          "secureContext": secureContext
      },
      "id": 0
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.text

#Query - read_house
def read_house(arg):
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "query",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name": '0bca8c9a73db7f25cfbdb3893ec7950f766e06e89d6edb1e1a9a94f93e957d56453ab629e1d47ae13d13b13457ebe793d25b00c33a5f56075f25f217ea8567fd'
          },
          "ctorMsg": {
             "function": "read_house",
             "args": [
                arg
             ]
          },
          "secureContext": secureContext
      },
      "id": 0
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.text

#Query - search_tran
def search_tran():
    url = blockchain_ibm + '/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "query",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name": function.Get_key()
          },
          "ctorMsg": {
             "function": "search_tran",
             "args": [
                "producer", "consumer", "type", "starttime"
             ]
          },
          "secureContext": secureContext
      },
      "id": 0
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.text

def get_chaincodeID_name():
    res_login = login()
    res_login = json.loads(res_login)

    if 'OK' not in res_login:
        return "failed login,failed login,failed login,failed login,failed login,failed login"

    res_deploy = deploy()
    res_deploy = json.loads(res_deploy)

    if 'result' not in res_deploy:
        return "failed deploy (result is not exist)"

    result_res_deploy = res_deploy['result']
    if result_res_deploy['status'] != 'OK':
        return "failed deploy (status is not OK)"
    else:
        message_result_res_deploy = result_res_deploy['message']
        print('Success login & deploy')

    print(message_result_res_deploy)
    function.Make_db_key(message_result_res_deploy)

    return function.Get_key()
