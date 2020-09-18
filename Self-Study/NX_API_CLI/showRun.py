import requests
import json

url='https://10.10.20.58/ins'
switchuser='admin'
switchpassword='Cisco123'

myheaders={'content-type':'application/json'}

payload={
  "ins_api":{
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show run",
    "output_format": "json"
    }
}

response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword), verify=False).json()
print(json.dumps(response, indent=1, sort_keys=True))