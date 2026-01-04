import requests

URL = "https://hdoom-box.onrender.com/"

r = requests.get(URL, timeout=10)
print("Pinged:", r.status_code)
