import requests
from flask import Flask, jsonify
import json
app = Flask(__name__)

@app.route('/json-api/version')
def version():
    with open('version.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/json-api/listpkgs')
def listpkgs():
    with open('listpkgs.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/json-api/changepackage')
def changepackage():
    with open('changepackage.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)
    
@app.route('/json-api/createacct')
def createacct():
    with open('createacct.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/json-api/suspendacct')
def suspendacct():
    with open('suspendacct.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)
    
@app.route('/json-api/unsuspendacct')
def unsuspendacct():
    with open('unsuspendacct.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)
    
@app.route('/json-api/removeacct')
def removeacct():
    with open('removeacct.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/json-api/passwd')
def passwd():
    with open('passwd.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)
    
@app.route('/json-api/checkavailable')
def checkavailable():
    return "1"

@app.route('/json-api/getuserdomains')
def getuserdomains():
    return '[["ACTIVE","subdomain.example.com"]]'

@app.route('/json-api/getdomainuser')
def getdomainuser():
    return '["ACTIVE","subdomain.example.com","/home/vol15_2/example.com/hname_12345678/htdocs","hname_12345678"]'

@app.route('/json-api/getcname')
def getcname():
    return '73081144a0525fde6ba1b0510684efcf'
    
@app.route('/json-api/supportnewticket')
def supportnewticket():
    return 'SUCCESS : 000000'
    
@app.route('/json-api/supportreplyticket')
def supportreplyticket():
    return 'SUCCESS'
    
if __name__ == '__main__':
   app.run(debug=True, port=2087)
