import os
import base64
import urllib.request
import urllib.error
import urllib.parse
import json

TOKEN = "YOUR_GITHUB_TOKEN"
REPO_NAME = "golf-club-comparison"

files_to_upload = [
    "index.html",
    "styles.css",
    "app.js",
    "data.js",
    "Data/Golf Comparison - Drivers.csv",
    "Data/Golf Comparison - Fairway.csv",
    "Data/Golf Comparison - Irons.csv",
    "Data/Golf Comparison - Wedges.csv",
]

def request(method, url, data=None):
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "python-script"
    }
    encoded_data = None
    if data:
        encoded_data = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=encoded_data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode()), None
    except urllib.error.HTTPError as e:
        return None, e

print("Authenticating with GitHub API...")
user_info, err = request("GET", "https://api.github.com/user")
if not user_info:
    print(f"Failed to get user. Check token. Error: {err.read() if err else 'Unknown'}")
    exit(1)
    
username = user_info['login']
print(f"Authenticated as {username}")

print(f"Creating repository '{REPO_NAME}'...")
repo_data = {
    "name": REPO_NAME,
    "description": "Dynamic Golf Club Comparison Website",
    "private": False,
    "auto_init": True
}
repo_info, err = request("POST", "https://api.github.com/user/repos", data=repo_data)
if not repo_info:
    err_body = err.read().decode()
    if "name already exists" in err_body.lower():
        print("Repo already exists, retrieving info...")
        repo_info, err2 = request("GET", f"https://api.github.com/repos/{username}/{REPO_NAME}")
        if not repo_info:
            print(f"Failed to find repo. Error: {err2}")
            exit(1)
    else:
        print(f"Failed to create repo. Error: {err_body}")
        exit(1)

html_url = repo_info.get('html_url', f"https://github.com/{username}/{REPO_NAME}")
default_branch = repo_info.get('default_branch', 'main')
print(f"Repository ready: {html_url}")
print(f"Default branch: {default_branch}")

for filepath in files_to_upload:
    if not os.path.exists(filepath):
        print(f"File not found on local disk: {filepath}")
        continue
    
    with open(filepath, "rb") as f:
        content = f.read()
    
    b64_content = base64.b64encode(content).decode('utf-8')
    
    # Path encoding specifically to handle spaces (using %20 instead of +)
    encoded_path = urllib.parse.quote(filepath.replace('\\', '/'))
    url = f"https://api.github.com/repos/{username}/{REPO_NAME}/contents/{encoded_path}"
    
    # Check if file exists to get sha for updating
    file_info, _ = request("GET", url + f"?ref={default_branch}")
    sha = file_info['sha'] if file_info and 'sha' in file_info else None
    
    data = {
        "message": f"Upload {filepath}",
        "content": b64_content,
        "branch": default_branch
    }
    if sha:
        data["sha"] = sha
        
    print(f"Uploading {filepath}...")
    res, err = request("PUT", url, data=data)
    if not res:
        print(f"  Failed: {err.read().decode()}")

print(f"\nSuccessfully populated repository at {html_url}!")
