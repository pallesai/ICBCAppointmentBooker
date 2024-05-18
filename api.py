import requests
import json
import yaml

login_end_point = "https://onlinebusiness.icbc.com/deas-api/v1/webLogin/webLogin"

with open('./config.yml', 'r') as file:
    conf = yaml.safe_load(file)


last_name = conf['icbc']['drvrLastName']
licence_number = conf['icbc']['licenceNumber']
keyword = conf['icbc']['keyword']

def get_bearer_token():

    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://onlinebusiness.icbc.com/webdeas-ui/login;type=driver',
        "Sec-Ch-Ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache, no-store",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    }

    payload = {
        "drvrLastName": last_name,
        "licenceNumber": licence_number,
        "keyword": keyword
    }

    response = requests.put(login_end_point, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        return response.headers["Authorization"]
    return ""
