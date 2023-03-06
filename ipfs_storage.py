import nft_storage
from nft_storage.api import nft_storage_api


def create_ipfs(object):
    configuration = nft_storage.Configuration(
        access_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDU2YzEyRTUzZTkwQTc1RUUwMTdkYWVDZTUyMzgyOEI2ZERFZjlhRUQiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY3NjE0NTk0ODgyOSwibmFtZSI6ImthbWFsZGVibmF0aCJ9.Uyn5j8ls2CvQosJyPmepqtGDrOgHLn9d_EBfhkwbHDg'
    )

    with nft_storage.ApiClient(configuration) as api_client:
        api_instance = nft_storage_api.NFTStorageAPI(api_client)

        with open(object, 'rb') as body:
            try:
                api_response = api_instance.store(body, _check_return_type=False)
                return api_response['value']['cid']
            except nft_storage.ApiException as e:
                print("Exception when calling NFTStorageAPI->store: %s\n" % e)
