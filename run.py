from cmklib import get_or_create_host
import json

json_response, created = get_or_create_host(
    ip="ip_address", host_name="hostname", folder="foldername")
print(json.dumps(json_response, indent=4, sort_keys=True))
