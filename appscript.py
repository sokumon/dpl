import requests
import json

def send_to_sheet(task,remarks,eodStatus):
    url = "https://script.google.com/macros/s/AKfycbxvo1Jb1MSRsQAeT7bLsw-sS4wwOKIXOqaXoBPylkSPj0slyJqYg1eMrLxBhstJiqIK/exec"

    payload = json.dumps({
    "task": task,
    "remarks": remarks,
    "eodStatus": eodStatus
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()



