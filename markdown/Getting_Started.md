# Getting Started

## The GDC Application Programming Interface (API): An Overview

The GDC API drives the GDC Data and Submission Portals and provides programmatic access to GDC functionality. This includes searching for, downloading, and submitting data and metadata. The GDC API uses JSON as its communication format, and standard HTTP methods like `GET`, `PUT`, `POST` and `DELETE`.

This guide explains how to construct and execute API requests and interpret API responses.

## Tools for communicating with the GDC API

Many third-party tools can be used for communicating with the GDC API and for preparing and visualizing API calls.

Examples of tools for communicating with the GDC API:

| Tool        | Type     |
| ------------- |-------------|
| [Curl](http://curl.haxx.se/docs/manpage.html) 		| Command line tool |
| [HTTPie](http://httpie.org) 	| Command line tool |
| [Postman REST Client](http://www.getpostman.com/) 														| App for Google Chrome and OS X |
| [DHC REST Client](http://restlet.com/products/dhc/)           | Google Chrome extension |
| [Google Chrome](http://www.google.com/chrome/) 	  | Google Chrome web browser |

Examples of tools that can help build GDC API calls:

| Tool        | Description     |
| ------------- |-------------|
| [JSONLint](http://jsonlint.com/)| Validate JSON |
| [JSON Formatter](http://jsonformatter.org/) | Format, validate, and convert JSON to other formats |
| [Percent-(URL)-encoding tool](https://codebeautify.org/url-encode-string)| Tool for percent-encoding strings |


## API Endpoints

Communicating with the GDC API involves making calls to API endpoints. Each GDC API endpoint represents specific API functionality, as summarized in the following table:

| Endpoint | Type | Description |
| --- | --- | --- |
| status | Status | Get the API status and version information |
| projects | Search & Retrieval | Search all data generated by a project |
| cases | Search & Retrieval | Find all files related to a specific case, or sample donor. |
| files | Search & Retrieval | Find all files with specific characteristics such as file_name, md5sum, data_format and others. |
| annotations | Search & Retrieval | Search annotations added to data after curation |
| data | Download | Used to download GDC data |
| manifest | Download | Generates manifests for use with GDC Data Transfer Tool |
| slicing | BAM Slicing | Allows remote slicing of BAM format objects |
| submission | Submission | Returns the available resources at the top level above programs i.e., registered programs |

The HTTP URL that corresponds to the latest version of a GDC API endpoint is `https://api.gdc.cancer.gov/<endpoint>`, where `<endpoint>` is the name of the endpoint.

The HTTP URL of an endpoint corresponding to a specific major version of the GDC API is `https://api.gdc.cancer.gov/<version>/<endpoint>`, where `<endpoint>` is the name of the endpoint and `<version>` is the GDC API version.

For example, the address of the latest version of the `status` endpoint is `https://api.gdc.cancer.gov/status`, whereas the address of the `status` endpoint corresponding to version 0 of GDC API is `https://api.gdc.cancer.gov/v0/status`.

### GDC Legacy Archive

To interact with data in the GDC Legacy Archive, add `legacy` to the endpoint URL before the `<endpoint>`:

	https://api.gdc.cancer.gov/legacy/<endpoint>

> __NOTE:__ The version can also be applied to a Legacy Archive search by placing the `<version>` before "/legacy/"

## Entity UUIDs

All objects (*entities*) in the GDC are assigned a unique identifier in the form of a [version 4 universally unique identifier (UUID)](https://en.wikipedia.org/wiki/Universally_unique_identifier). The UUID uniquely identifies the entity in the GDC, and is stored in the entity's `id` property.

UUIDs are frequently used in GDC API requests and responses to identify specific entities like files, cases, and samples.

See [GDC Data Model](../../Data/Data_Model/GDC_Data_Model.md) for details.

## Sample Request

The following is an example of a request to the `files` endpoint, which retrieves information about a BAM file stored in the GDC.

``` shell
curl https://api.gdc.cancer.gov/files/d853e541-f16a-4345-9f00-88e03c2dc0bc?pretty=true
```
``` python
import requests
import json

file_endpt = 'https://api.gdc.cancer.gov/files/'
file_uuid = 'd853e541-f16a-4345-9f00-88e03c2dc0bc'
response = requests.get(file_endpt + file_uuid)

# OUTPUT METHOD 1: Write to a file.
file = open("sample_request.json", "w")
file.write(response.text)
file.close()

# OUTPUT METHOD 2: View on screen.
print(json.dumps(response.json(), indent=2))
```
[Download Script](scripts/Sample_Request.py)
## Authentication

Authentication is required for downloading controlled-access data, and for all data submission functionality. The GDC API uses tokens for authentication.

Users can obtain authentication tokens from the [GDC Data Portal](https://portal.gdc.cancer.gov) and the [GDC Data Submission Portal](https://portal.gdc.cancer.gov/submission). See the [GDC Data Portal User's Guide](../../Data_Portal/Users_Guide/Repository.md#gdc-authentication-tokens) and the [GDC Data Submission Portal User's Guide](../../Data_Submission_Portal/Users_Guide/Data_Submission_Process.md#authentication) for instructions.

### Using Authentication Tokens

All API requests that require authentication must include a token as an `X-Auth-Token` custom HTTP header.

In the following example, an authentication token is saved as an environment variable and passed to `curl` to download a controlled-access file:

```Shell
token=$(cat <gdc-token-text-file.txt>)

curl -O -J -H "X-Auth-Token: $token" 'https://api.gdc.cancer.gov/data/a1c1b23b-cc41-4e85-b1b7-62a42873c5af'
```
```Shell Output
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 31.4M  100 31.4M    0     0   290k      0  0:01:50  0:01:50 --:--:--  172k
curl: Saved to filename 'ACOLD_p_TCGA_Batch17_SNP_N_GenomeWideSNP_6_A03_466078.tangent.copynumber.data.txt'
```
```Python
import requests
import json
import re

'''
 This script will not work until $TOKEN_FILE_PATH
 is replaced with an actual path.
'''

with open("$TOKEN_FILE_PATH","r") as token:
    token_string = str(token.read().strip())

headers = {
           'X-Auth-Token': token_string
          }

data_endpt = 'https://api.gdc.cancer.gov/data/'
data_uuid = 'a1c1b23b-cc41-4e85-b1b7-62a42873c5af'
headers = {
           'X-Auth-Token': token_string
          }
response = requests.get(data_endpt + data_uuid, headers=headers)

# The file name can be found in the header within the Content-Disposition key.
response_head_cd = response.headers["Content-Disposition"]

file_name = re.findall("filename=(.+)", response_head_cd)[0]

with open(file_name, "wb") as output_file:
    output_file.write(response.content)
```
[Download Python Script](scripts/Authentication_Tokens.py)


For more information about authentication tokens, including token expiration and rotation, see [Data Security](../../Data/Data_Security/Data_Security.md#authentication-tokens).

>**NOTE:** The authentication token should be kept in a secure location, as it allows access to all data accessible by the associated user account.