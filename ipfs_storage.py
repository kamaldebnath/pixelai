import nft_storage,os
from nft_storage.api import nft_storage_api


def create_ipfs(object):
    configuration = nft_storage.Configuration(
        access_token=os.environ.get('NFT_STORAGE_API')

    )

    with nft_storage.ApiClient(configuration) as api_client:
        api_instance = nft_storage_api.NFTStorageAPI(api_client)

        with open(object, 'rb') as body:
            try:
                api_response = api_instance.store(body, _check_return_type=False)
                return api_response['value']['cid']
            except nft_storage.ApiException as e:
                print("Exception when calling NFTStorageAPI->store: %s\n" % e)
