import urllib.request
import tarfile
import os

url = 'https://github.com/supabase/cli/releases/download/v2.84.2/supabase_windows_amd64.tar.gz'
filename = 'supabase.tar.gz'

print("Downloading Supabase CLI...")
urllib.request.urlretrieve(url, filename)

print("Extracting...")
with tarfile.open(filename, "r:gz") as tar:
    tar.extractall()

os.remove(filename)
print("Supabase CLI installed successfully in the current folder!")
