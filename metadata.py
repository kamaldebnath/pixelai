import json
from moralis import evm_api
import base64
import os

api_key = os.environ.get("MORALIS_API")


def createMetadata(imagelink, description):
    content = {
        "image": f"ipfs://{imagelink}",
        "description": description,
    }
    body = [
        {
            'path': 'metadata.json',
            'content': base64.b64encode(bytes(json.dumps(content), 'ascii')).decode('ascii')
        }
    ]

    res = evm_api.ipfs.upload_folder(api_key, body)[0]["path"]
    return res
