import os
import requests

import replicate
from PIL import Image

os.environ["REPLICATE_API_TOKEN"] = "ae2755d9db6fbb6b75a2dc680fabb0ca3de158db"
model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get("db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf")


def create(prompt):
    file = version.predict(**{
        'prompt': prompt,
        'image_dimensions': "768x768",
        'num_outputs': 1,
        'num_inference_steps': 50,
        'guidance_scale': 7.5,
        'scheduler': "DPMSolverMultistep",
    })[0]
    img = Image.open(requests.get(file, stream=True).raw)
    img.save(f"./images/{prompt[0:4]}.png")
    return file