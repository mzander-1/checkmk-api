from cmklib import get_or_create_host
import json

json_response, created = get_or_create_host(ip="188.34.181.225", host_name="testtest", folder="test")
print(json.dumps(json_response, indent=4, sort_keys=True))