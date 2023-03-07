import createimage, metadata, ipfs_storage,cleardata
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='images')


@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        promt = request.form["promt"]
        if promt:
            img_link = createimage.create(prompt=promt)
            # ipfs_img = ipfs_storage.create_ipfs(f'./images/{promt[0:4]}.png')
            ipfs_img= ipfs_storage.pinata_ipfs(f'./images/{promt[0:4]}.png')
            nft_metadata = metadata.createMetadata(ipfs_img, promt)
            cleardata.remove(promt[0:4])
            return render_template("home.html", nft_metadata=nft_metadata,file_name=img_link)
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
