import json
from moralis import evm_api
import base64

api_key = 'Qs9PMJRRU6Xk3SYEDTWWegs7CQZgbbwAVaneZQJ8hDOv89v3ISVmdrqbCRz9cUZo'


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

