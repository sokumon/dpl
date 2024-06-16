import requests
import json
from dpl.config import *
def send_to_sheet(task,remarks,eodStatus):
    url = reader()
    if url is None:
        return None

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



