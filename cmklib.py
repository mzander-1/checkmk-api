#!/usr/bin/env python3
import pprint, requests, json, os
from dotenv import load_dotenv

load_dotenv()
HOST_NAME = "192.168.0.82"
SITE_NAME = "hatraco"
API_URL = f"http://{HOST_NAME}/{SITE_NAME}/check_mk/api/1.0"

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

def get_host(host_name):
    session = requests.session()
    session.headers['Authorization'] = f"Bearer {USERNAME} {PASSWORD}"
    session.headers['Accept'] = 'application/json'

    resp = session.get(
        f"{API_URL}/objects/host_config/{host_name}",
        params={  # goes into query string
            "effective_attributes": False,  # Show all effective attributes on hosts, not just the attributes which were set on this host specifically.
        },
    )
    if resp.status_code == 200:
        return resp.json()

    raise RuntimeError(pprint.pformat(resp.json()))

def check_folder_exists(folder):

    session = requests.session()
    session.headers['Authorization'] = f"Bearer {USERNAME} {PASSWORD}"
    session.headers['Accept'] = 'application/json'

    resp = session.get(
        f"{API_URL}/objects/folder_config/{folder}",
        params={  
            "show_hosts": False,},
    )
    return resp.status_code == 200

def create_folder(folder):

    session = requests.session()
    session.headers['Authorization'] = f"Bearer {USERNAME} {PASSWORD}"
    session.headers['Accept'] = 'application/json'

    resp = session.post(
        f"{API_URL}/domain-types/folder_config/collections/all",
        headers={
            "Content-Type": 'application/json', 
        },
        json={
            "name": folder,
            "title": folder,
            "parent": "/",
            "attributes": "",
        },
    )
    result = resp.json()
    return resp.status_code == 200 or result["detail"].find("already exists") > -1
    

def get_or_create_host(ip, host_name, folder):

    session = requests.session()
    session.headers['Authorization'] = f"Bearer {USERNAME} {PASSWORD}"
    session.headers['Accept'] = 'application/json'

    if not check_folder_exists(folder):
        if not create_folder(folder):
            print("Unable to create folder. Aboarting.")
            return

    resp = session.post(
        f"{API_URL}/domain-types/host_config/collections/all",
        params={  
            "bake_agent": False,  
        },
        headers={
            "Content-Type": 'application/json',  
        },
        json={
            "folder": "/" + folder,
            "host_name": host_name,
            "attributes": {
                "ipaddress": ip
            },
        },
    )
    if resp.status_code == 200:
        return resp.json(), True

    
    result = resp.json()
    result_as_string = json.dumps(result)

    if result_as_string.find("already exists") > -1:
        return get_host(host_name), False
    
    raise RuntimeError("Unhandled Exception. Consult your Developer.")
    

