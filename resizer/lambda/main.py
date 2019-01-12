import os
import urllib
from PIL import Image

lst = [256,512,1024,2048,4096,8192,16384]

def download_image(url):
    urllib.urlretrieve(url, "/tmp/"+url.split("/")[-1])

def resize_image(imgpath,final_path):
    im = Image.open(imgpath)
    width, height = im.size
    width = min(lst, key=lambda x:abs(x-width))
    height = min(lst, key=lambda x:abs(x-height))
    im = im.resize((width, height))
    im.save(final_path)
    return "Success"
    
# def upload_image(imgpath):
#     imgname = imgpath.split("/")[-1]
#     with open(imgpath, 'rb') as data:
#         conf_file = {imgname: data}
#         r = requests.post("https://transfer.sh/", files=conf_file)
#         return r.text

def remove_image(image1,image2):
    os.remove(image1)
#     os.remove(image2)

def handler(event,context):
    fle = event
    image_url = fle["image_url"]
    image_path = "/tmp/"+image_url.split("/")[-1]
    imgname = image_path.split("/")[-1]
    final_path = "/tmp/"+imgname.split(".")[0]+"_resized"+"."+imgname.split(".")[-1]
    download_image(image_url)
    response = resize_image(image_path,final_path)
#     response = upload_image(final_path)
    remove_image(image_path,final_path)
    return response