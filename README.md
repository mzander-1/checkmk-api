
# Check MK API Wrapper

This Python API wrapper provides convenient methods to interact with the Check MK monitoring system API. It allows you to perform various operations such as retrieving host configurations, checking folder existence, creating folders, and creating hosts.

## Prerequisites

- Python 3.x
- `requests` library
- `dotenv` library (for loading environment variables from a `.env` file)

## Installation

1. Clone or download this repository to your local machine.

2. Install the required libraries using pip:

   ```bash
   pip install requests python-dotenv
   ```

## Configuration

1. Ensure you have access to a Check MK instance with API access enabled.

2. Create a `.env` file in the project directory with the following variables:

   ```dotenv
   USERNAME=your_check_mk_username
   PASSWORD=your_check_mk_password
   ```

   Replace `your_check_mk_username` and `your_check_mk_password` with your Check MK credentials.

## Functions

- `get_host(host_name)`: Retrieve the configuration of a specific host.
- `check_folder_exists(folder)`: Check if a folder exists in Check MK.
- `create_folder(folder)`: Create a folder in Check MK.
- `get_or_create_host(ip, host_name, folder)`: Get the configuration of a host. If the host does not exist, create it.

## Notes

- This API wrapper assumes that you have already set up Check MK with appropriate access rights for the provided credentials.
- Ensure that your Check MK instance is accessible from the machine running this API wrapper.
Here's an updated README specifically for the `run.py` script:

---

# Check MK API Runner

This Python script `run.py` is used to run the Check MK API wrapper and interact with a Check MK monitoring system. It calls the `get_or_create_host` function from the `cmklib` module to either retrieve the configuration of a host or create a new host if it doesn't exist.

## Prerequisites

- Python 3.x
- `cmklib` module (the API wrapper module)
- `json` module (for handling JSON responses)

## Usage

1. Ensure you have configured the Check MK API wrapper as described in the [API wrapper README](#check-mk-api-wrapper).

2. Modify the `run.py` script as needed, providing the appropriate values for the `ip_address`, `hostname`, and `foldername`.

3. Run the `run.py` script:

   ```bash
   python run.py
   ```

4. The script will call the `get_or_create_host` function and print the JSON response with indentation and sorted keys.

## Example

```python
from cmklib import get_or_create_host
import json

# Replace the values below with your actual data
ip_address = "192.168.1.100"
hostname = "example_host"
foldername = "example_folder"

# Call get_or_create_host function
json_response, created = get_or_create_host(ip=ip_address, host_name=hostname, folder=foldername)

# Print JSON response
print(json.dumps(json_response, indent=4, sort_keys=True))
```

## Notes

- Ensure that the `cmklib` module is accessible from the `run.py` script. You may need to adjust the import statement accordingly if the module is located in a different directory.
- Make sure that the `run.py` script has the appropriate permissions to execute and access the necessary files and resources.

