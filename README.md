* [PyPI](https://pypi.org/project/VUMP-gRPC-client/) 


# VUMP-gRPC-client
This is a python gRPC client for V2Ray/V2Fly gRPC API.


## Installation
```shell
pip install -U VUMP-gRPC-client
```


## Example
```python
from vump_grpc_client import VUMPClient, utils, exceptions

v2ray_client = VUMPClient('1.2.3.4', 1234)
user_id = utils.generate_random_user_id()
user_email = utils.generate_random_email()
inbound_tag = 'inbound-tag'

# Get stats
print(utils.human_readable_bytes(v2ray_client.get_client_download_traffic('user-email@mail.com')))
print(utils.human_readable_bytes(v2ray_client.get_client_upload_traffic('user-email@mail.com')))
print(utils.human_readable_bytes(v2ray_client.get_inbound_download_traffic(inbound_tag)))
print(utils.human_readable_bytes(v2ray_client.get_inbound_upload_traffic(inbound_tag)))
print(utils.human_readable_bytes(v2ray_client.get_total_download_traffic()))
print(utils.human_readable_bytes(v2ray_client.get_total_upload_traffic()))

# Add & Remove client
user = v2ray_client.add_client(inbound_tag, user_id, user_email)
if user:
    print(user)
    v2ray_client.remove_client(inbound_tag, user_email)

# restart logger
v2ray_client.restart_logger()
```