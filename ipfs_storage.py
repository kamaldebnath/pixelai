# import nft_storage
# from nft_storage.api import nft_storage_api
#
#
# def create_ipfs(object):
#     configuration = nft_storage.Configuration(
#         access_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDU2YzEyRTUzZTkwQTc1RUUwMTdkYWVDZTUyMzgyOEI2ZERFZjlhRUQiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY3NjE0NTk0ODgyOSwibmFtZSI6ImthbWFsZGVibmF0aCJ9.Uyn5j8ls2CvQosJyPmepqtGDrOgHLn9d_EBfhkwbHDg'
#     )
#
#     with nft_storage.ApiClient(configuration) as api_client:
#         api_instance = nft_storage_api.NFTStorageAPI(api_client)
#
#         with open(object, 'rb') as body:
#             try:
#                 api_response = api_instance.store(body, _check_return_type=False)
#                 return api_response['value']['cid']
#             except nft_storage.ApiException as e:
#                 print("Exception when calling NFTStorageAPI->store: %s\n" % e)


import pinata

pinata = pinata.Pinata("4c8e669486859c93ecc2","9d32b02c12e235e9bfc66b85e55a1f5f1a49b92f23c3a386664dfe14cccf15ce","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiIwYTYxYWRmYS00MjE0LTRiZDktYTI4OS00YTJhMTRiOGNjMDUiLCJlbWFpbCI6ImZmZDAwNzc3QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImlkIjoiRlJBMSIsImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxfSx7ImlkIjoiTllDMSIsImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxfV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2UsInN0YXR1cyI6IkFDVElWRSJ9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiI0YzhlNjY5NDg2ODU5YzkzZWNjMiIsInNjb3BlZEtleVNlY3JldCI6IjlkMzJiMDJjMTJlMjM1ZTliZmM2NmI4NWU1NWExZjVmMWE0OWI5MmYyM2MzYTM4NjY2NGRmZTE0Y2NjZjE1Y2UiLCJpYXQiOjE2NzgxNzA1NzR9.8Itz4Nd32wsQZmALCBwGM6oP5Fo__TXoAYFzJrmReRo")

def pinata_ipfs(object):
    file=pinata.pin_file(object)
    return file