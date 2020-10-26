import requests 
import json
import sys 


Auth_key = {"x-apikey": "accesskey=#ACCESSKEY#; secretkey=#SECRETKEY#"}
policy_id = 0
repository_id = 0
scanResult_id = '0'
scanStatus = ''
target = str(sys.argv[1])
target_name=#SCAN NAME#
# you can use "target" so the scan will be named by the target IP

# getting the scan policy id 

try:
	resp = requests.get('https://#TENABLESC IP:PORT#/rest/policy',headers=Auth_key,verify=False)
	for obj in resp.json()["response"]["usable"]:
		if ( str(obj['name']) == '#POLICY NAME#'):
		policy_id = (obj['id'])
except requests.exceptions.RequestException as e: 
	print("Can't get the scan policy id!")
	raise SystemExit(e)

# getting the repository id

try:
	resp = requests.get('https://#TENABLESC IP:PORT#/rest/repository',headers=Auth_key,verify=False)
	for obj in resp.json()["response"]:
		if (obj["name"] == '#REPOSITORY NAME#'):
		repository_id = obj["id"]
except requests.exceptions.RequestException as e: 
	print("Can't get repository id!")
	raise SystemExit(e)

# create the scan

scan = scan = {
    "name" : target_name,
    "type" : "policy",
    "description" : "",
    "repository" : {
        "id" : repository_id
    },
   
    "policy" : {
    "id" : policy_id
    },
    "dhcpTracking" : "false",
    "classifyMitigatedAge" : "0",
    "schedule" : {
        "type" : "never"
    },
    "reports" : [],
    "assets" : [],
    "credentials" : [],
    "emailOnLaunch" : "false",
    "emailOnFinish" : "false",
    "timeoutAction" : "import",
    "scanningVirtualHosts" : "false",
    "rolloverType" : "template",
    "ipList" : target,
    "maxScanTime" : "3600"
}

try:
	resp = requests.post('https://#TENABLESC IP:PORT#/rest/scan',headers=Auth_key,json=scan,verify=False)
	scan_id = resp.json()["response"]["id"]
except requests.exceptions.RequestException as e: 
	print("Can't create the scan!")
	raise SystemExit(e)

# lunch the scan

url = 'https://#TENABLESC IP:PORT#/rest/scan/'+scan_id+'/launch'
try:
	resp = requests.post(url,headers=Auth_key,json=scan,verify=False)
	scanResult_id = resp.json()["response"]["scanResult"]["id"]
except requests.exceptions.RequestException as e: 
	print("Can't launch the scan!")
	raise SystemExit(e)
