import urllib.request
url = "https://dlzuupgceexxvqmwzehz.supabase.co/rest/v1/"
headers = {
    "apikey": "sb_publishable_VrZLoXbjxPUcPAhFQxlgOg_uY45slHG",
    "Authorization": "Bearer sb_publishable_VrZLoXbjxPUcPAhFQxlgOg_uY45slHG"
}
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        print("Success:", response.status)
        print(response.read().decode())
except Exception as e:
    print("Error:", e)
