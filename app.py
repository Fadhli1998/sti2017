#!flask/bin/python

from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth
from flask import make_response

import requests, json

auth = HTTPBasicAuth()
app = Flask(__name__)

@auth.get_password
def get_password(username):
	if username == 'admin':
	   return 'python'
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error':'Unauthorized access'}), 401)

@app.route('/rackhd/login', methods=['POST'])
@auth.login_required
def rackhd_login():
	if not request.json or not 'username' in request.json:
		abort(400)

	user =  request.json['username']
	pw = request.json['password']
	
	url = "https://localhost:8443/login"
	payload = '{"username" : "' + user + '", "password" : "' + pw +'"}'
	
	headers= {
		"Content-Type": "application/json"
	}

	r = requests.post(url, headers=headers, data=payload, verify=False)
	return r.text

@app.route('/rackhd/skus/read', methods=['GET'])
@auth.login_required
def read_skus():
	url = "https://localhost:8443/api/current/skus"

	token = "JWT " + request.headers.get('token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	r = requests.get(url, headers=headers, verify=False)
	return r.text

@app.route('/rackhd/skus/update', methods=['PATCH'])
@auth.login_required
def update_skus():
	base_url = "https://localhost:8443/api/current/skus"

	skuId = request.json['skuId']

	url = base_url + "/" + skuId

	token = "JWT " + request.headers.get('token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	field = request.json['field']
	data = request.json['data']
	
	payload = '{"%s":"%s"}' % (field,data)	
	
	r = requests.patch(url, headers=headers, data=payload, verify=False)

	return r.text

@app.route('/rackhd/skus/create', methods=['POST'])
@auth.login_required
def create_skus():
        url = "https://localhost:8443/api/current/skus"

        token = "JWT " + request.headers.get('token')

        headers = {
                "Content-Type": "application/json",
                "Authorization": token
        }

        name = request.json['name']
        path = request.json['path']
        path2 = request.json['path2']
	contains = request.json['contains']
	equals = request.json['equals']
        discoveryGraphName = request.json['discoveryGraphName']
        username = request.json['username']
	password = request.json['password']
        hostname = request.json['hostname']

        payload = '{"name":"' + name + '", "rules": [{"path":"' + path + '", "contains": "' + contains + '"},{"path":"' + path2 + '", "equals":"' + equals +'"}], "discoveryGraphName": "' + discoveryGraphName + '", "discoveryGraphOptions": {"username":"' + username + '", "password":"' + password + '", "hostname":"' + hostname + '"}}'

        r = requests.post(url, headers=headers, data=payload, verify=False)
        return r.text


@app.route('/rackhd/skus/delete', methods=['DELETE'])
@auth.login_required
def delete_skus():

        base_url = "https://localhost:8443/api/current/skus"

	skuId = request.json['skuId']

	url = base_url + "/" + skuId
	
        token = "JWT " + request.headers.get('token')

        headers = {
                "Content-Type": "application/json",
                "Authorization": token
       	}

        r = requests.delete(url, headers=headers, verify=False)
        return r.text

@app.route('/rackhd/metricpollers/read', methods=['GET'])
@auth.login_required
def read_metricpollers():
        url = "https://localhost:8443/api/current/pollers"

        token = "JWT " + request.headers.get('token')

        headers = {
                "Content-Type": "application/json",
                "Authorization": token
        }

        r = requests.get(url, headers=headers, verify=False)
        return r.text

@app.route('/rackhd/metricpollers/create', methods=['POST'])
@auth.login_required
def create_metricpollers():
        url = "https://localhost:8443/api/current/pollers"

        token = "JWT " + request.headers.get('token')

        headers = {
                "Content-Type": "application/json",
                "Authorization": token
        }

        type = request.json['type']
	node = request.json['node']
	metric = request.json['metric']

	payload = '{"type":"' + type + '", "pollInterval":1000, "node":"' + node + '", "config": {"metric":"' + metric +'"}}'

        r = requests.post(url, headers=headers, data=payload, verify=False)
        return r.text

@app.route('/rackhd/metricpollers/update', methods=['PATCH'])
@auth.login_required
def update_metricpollers():
        base_url = "https://localhost:8443/api/current/pollers"

        pollerId = request.json['pollerId']

        url = base_url + "/" + pollerId

        token = "JWT " + request.headers.get('token')

        headers = {
                "Content-Type": "application/json",
                "Authorization": token
        }

        field = request.json['field']
        data = request.json['data']

        payload = '{"%s":"%s"}' % (field,data)

        r = requests.patch(url, headers=headers, data=payload, verify=False)

        return r.text

@app.route('/rackhd/metricpollers/delete', methods=['DELETE'])
@auth.login_required
def delete_metricpollers():

        base_url = "https://localhost:8443/api/current/pollers"

        pollerId = request.json['pollerId']

        url = base_url + "/" + pollerId

        token = "JWT " + request.headers.get('token')

        headers = {
                "Content-Type": "application/json",
                "Authorization": token
        }

        r = requests.delete(url, headers=headers, verify=False)
        return r.text

if __name__ == '__main__':
	app.run(debug=True)
