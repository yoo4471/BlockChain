from flask import render_template, flash, redirect, request, Response
from app import app
import json, requests
from . import function


blockchain_ibm = 'https://bd7bb099c91b4431bebb40f21abc39a5-vp0.us.blockchain.ibm.com:5002'
chaincodeID_path = "https://github.com/yoo4471/last_chaincode"

enrollId = 'user_type1_4'
enrollSecret = '4a238b38ec'
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
		   "name": function.Get_key()
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
def modify_petsitter(arg):
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
		  "function": "modify_petsitter",
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

#INVOKE - delete_petsitter
def delete_petsitter(arg):
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
		  "function": "delete_petsitter",
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

#INVOKE - save_home_address
def save_home_address(arg):
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
		   "name": function.Get_key()
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
		   "name": function.Get_key()
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
def modify_home_address(arg):
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

#INVOKE - modify_home_room
def modify_home_room(arg):
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

#INVOKE - modify_home_car_elevator
def modify_home_car_elevator(arg):
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


#INVOKE - save_tran
def save_tran(arg):
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
				arg[0], arg[1], arg[2], arg[3], arg[4], arg[5], arg[6], arg[7]
			 ]
		  },
		  "secureContext": secureContext
	  },
	  "id": 0
	}
	headers = {'content-type': 'application/json'}
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	return r.text

#INVOKE - delete_house
def delete_house(arg):
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
			"function": "delete_house",
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

#INVOKE - save_home
def save_home(arg):
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
		  "function": "save_home",
		  "args": [
			arg[0], arg[1], arg[2], arg[3], arg[4], arg[5], arg[6], arg[7], arg[8], arg[9]
		  ]
		},
		"secureContext": secureContext
	 },
	 "id": 0
   }
   headers = {'content-type': 'application/json'}
   r = requests.post(url, data=json.dumps(payload), headers=headers)
   return r.text

#INVOKE - modify_home
def modify_home(arg):
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
		  "function": "modify_home",
		  "args": [
			arg[0], arg[1], arg[2], arg[3], arg[4], arg[5], arg[6], arg[7], arg[8], arg[9]
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
def read_petsitter(arg):
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

#Query - read_house
def read_house(arg):
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
def search_tran(arg):
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

#Query - search_bytotal
def search_bytotal(arg):
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
		"function": "search_bytotal",
		"args": [
		 arg[0], arg[1], arg[2], arg[3], arg[4], arg[5], arg[6]
		]
	  },
	  "secureContext": secureContext
	},
	"id": 0
   }
   headers = {'content-type': 'application/json'}
   r = requests.post(url, data=json.dumps(payload), headers=headers)
   return r.text

#Query - search_byregion
def search_byregion(arg):
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
		"function": "search_byregion",
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
