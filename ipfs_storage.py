import pinata,os

pinata = pinata.Pinata(os.environ.get('PINATA_API'), os.environ.get("PINATA_SECRET_KEY"),os.environ.get("PINATA_ACCESS_TOKEN"))


def pinata_ipfs(object):
    file = pinata.pin_file(object)
    return file['data']['IpfsHash']
