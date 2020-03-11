import os
import requests
import csv
import shutil

def download(url, to=None):
    """Method for downloading file through URL

    :param url: str
          URL pointing to a remote file.

    :param to: str
          Local path, absolute or relative, with a filename 
          to the file storing the contents of the remote file.
    """
    if os.path.isfile("./" + url.split("/")[-1]):
        print("File already exists")
        exit()

    response = requests.get(url)
    with open(os.path.join("./", url.split("/")[-1]), 'wb') as f:
        print('Downloading file to ./' + url.split("/")[-1])
        f.write(response.content)


def altDownload(url, to=None):
    """Alternative method to above method"""
    r = requests.get(url, verify=False,stream=True)
    if r.status_code!=200:
        print("Failure!!")
        exit()
    else:
        r.raw.decode_content = True
        with open(os.path.join("./", url.split("/")[-1]), 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print("Success")
