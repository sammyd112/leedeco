import cloudinary 
import os

cloudinary.config(
  cloud_name = "dbdyyg3uy",
  api_key = os.environ['API_KEY'],
  api_secret = os.environ['API_SECRET'],
  secure = True
)
import cloudinary.uploader
import cloudinary.api

#for key, value in images.photos.items():
    #upload(f"{value}", public_id=f"{key}")