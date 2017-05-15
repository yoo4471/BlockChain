from flask import render_template, flash, redirect, request, Response
from app import app
import json, requests
from . import function


blockchain_ibm = 'https://26f0206924e9422dbb67e806b70a5474-vp0.us.blockchain.ibm.com:5004'
chaincodeID_path = "https://github.com/liil93/new_chaincode"

enrollId = 'user_type2_3'
enrollSecret = '97fbf47518'
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

#INVOKE - UserRegist
def UserRegist():
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
             "function": "UserRegist",
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

#INVOKE - UserChangeContact
def UserChangeContact():
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
             "function": "UserChangeContact",
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

#INVOKE - AssetRegist
def AssetRegist():
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
             "function": "AssetRegist",
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

#INVOKE - AssetChange
def AssetChange():
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
             "function": "AssetChange",
             "args": [
                "userID", "sceretkey", "starttime", "endtime", "except"
             ]
          },
          "secureContext": secureContext
      },
      "id": 0
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.text

#INVOKE - AssetDelete
def AssetDelete():
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
             "function": "AssetDelete",
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

#INVOKE - TransactionRegist
def TransactionRegist():
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
             "function": "TransactionRegist",
             "args": [
                "producer", "secretkey", "consumer", "type", "starttime", "endtime", "cost"
             ]
          },
          "secureContext": secureContext
      },
      "id": 0
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.text

#Query - UserRead
def UserRead():
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
             "function": "UserRead",
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

#Query - AssetRead
def AssetRead():
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
             "function": "AssetRead",
             "args": [
                "assetkey"
             ]
          },
          "secureContext": secureContext
      },
      "id": 0
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.text

#Query - TransactionRead
def TransactionRead():
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
             "function": "TransactionRead",
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

#Query - LocateSearch
def LocateSearch():
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
             "function": "LocateSearch",
             "args": [
                "Seoul"
             ]
          },
          "secureContext": secureContext
      },
      "id": 0
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.text

#Query - GetUpdate
def GetUpdate():
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
             "function": "GetUpdate",
             "args": [""]
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
