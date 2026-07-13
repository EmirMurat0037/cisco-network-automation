import base64
import requests

username="admin" 
password="Cisco123"

raw_credentials=f"{username}:{password}"

bytes_data = raw_credentials.encode("utf-8")
encoded_bytes = base64.b64encode(bytes_data)

auth_token = encoded_bytes.decode("utf-8")

print(f"Security Token Generated Succesfully:{auth_token}")

request_headers = {
    "Authorization": f"Basic {auth_token}",
    "Accept": "application/yang-data+json"
}
