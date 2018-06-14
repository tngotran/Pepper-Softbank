# import requests

Musio_url = "https://ai.themusio.com/chat/send/"
jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE0ODg1MjM1NDEsImNsaWVudF9rZXkiOiIybVp3cUFQYUh5TnRSR2l4NFpVZ3FMME8wR1BOWUw0OXZUZ2RwMG1SdHRFaG5DblQ2UkVJRVJ6Yjd4Y24zaUlpR3lWVFVvVHA2a1hid0Rzb0dhZHpsUlJONXpVODczdHk2Z0JPMWIzdFRGNmhvR2U5SEt4M3laZjdOOXJEcWxnYSIsImVtYWlsIjoiakBha2EuY29tIiwiZXhwIjoxNDkzNzA3NTQxLCJpZCI6NTAxfQ.t7PeLgAnSrUXeBFg8vnU0sxamf5ZbIYZqGfcIga3Kxs"
# user_id = "0"
# MusioResponse = "default text"


# # params = {"access_token": ACCESS_TOKEN_PAGE}
# #headers = {"Content-Type": "application/json"}
# headers = {'Authorization': 'Bearer' + jwt, 'Content-Type': 'application/json'}
# params = {'member_id': 0, 'candidates': 'hello, where are you from','cleverness':0}

# cookies = None

# r = requests.post(Musio_url, data=params, headers=headers, cookies=cookies)
# print(r.url)
# if r.status_code != 200:
#     print(r.status_code)
#     print(r.text)


import requests
import json


user_sent = "what are you doing"
member_id = 0
cookies = None

headers = {"Authorization":"Bearer "+jwt}
data = {"candidates":user_sent,
        "member_id":member_id,
        "cleverness":0}
        
http_resp = requests.post(Musio_url,data=data,headers=headers,cookies=cookies)

if http_resp.status_code != 200:
    print(http_resp.status_code)
    print(http_resp.text)

cookies = http_resp.cookies

recei_obj = json.loads(http_resp.text)
# print(http_resp.text)
emotion = recei_obj['data']['emotions']['musio']['emotion']
reply = recei_obj['data']['musio_text']['message']

print(reply)