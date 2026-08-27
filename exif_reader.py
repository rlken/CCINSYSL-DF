# exif_reader.py
import piexif
import urllib.request

image_url = 'https://www.w3schools.com/w3css/img_lights.jpg'
image_path = 'sample_image.jpg'

print(f"Downloading sample image from {image_url}...")
request = urllib.request.Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(request) as response, open(image_path, 'wb') as out_file:
    out_file.write(response.read())

try:
    exif_dict = piexif.load(image_path)
except Exception as e:
    print(f"Error reading EXIF data: {e}")
    exit()

print("\nEXIF Metadata Analysis:")

make = exif_dict.get('0th', {}).get(piexif.ImageIFD.Make)
model = exif_dict.get('0th', {}).get(piexif.ImageIFD.Model)
date_time_original = exif_dict.get('Exif', {}).get(piexif.ExifIFD.DateTimeOriginal)

print(f"Camera Make: {make.decode('utf-8').strip() if make else 'Not found'}")
print(f"Camera Model: {model.decode('utf-8').strip() if model else 'Not found'}")
print(f"Date/Time Original: {date_time_original.decode('utf-8').strip() if date_time_original else 'Not found'}")