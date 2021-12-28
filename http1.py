import requests

host = "https://b2ef45f8-e166-41d7-bd35-9ad159028fbf.mock.pstmn.io/test"
res = requests.get(host)

print(res.status_code)
print(res.raise_for_status())
print(res.text)
print(res.content)