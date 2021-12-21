# /Users/johnlee/Downloads/20211221_125748.jpg

from PIL import Image
from PIL.ExifTags import TAGS
import webbrowser

file_path = input("[*] Enter the Absolute Path > ")
image = Image.open(file_path)
info = image._getexif()
image.close()

tag_label = {}

for tag, value in info.items():
    decoded = TAGS.get(tag, tag)
    tag_label[decoded] = value

################# print maker

exif_maker = tag_label['Make']
print("[*] Maker : %s" % exif_maker)

################# print model name

exif_model = tag_label['Model']
print("[*] Model Name: %s" % exif_model)

################# print (lat, lon)

exif_GPS = tag_label['GPSInfo']
latitude_data = exif_GPS[2]
longitude_data = exif_GPS[4]

latitude_degree = int(latitude_data[0])
latitude_minute = int(latitude_data[1])
latitude_second = float(latitude_data[2])

longitude_degree = int(longitude_data[0])
longitude_minute = int(longitude_data[1])
longitude_second = float(longitude_data[2])

print_latitude = str(latitude_degree) + "°" + str(latitude_minute) + "'" + str(latitude_second) + "\"" + exif_GPS[1]
print_longitude = str(longitude_degree) + "°" + str(longitude_minute) + "'" + str(longitude_second) + "\"" + exif_GPS[3]

print("[*] %s, %s" % (print_latitude, print_longitude))

################# print map with (lat, lon)

latitude = str(latitude_degree + (latitude_minute + latitude_second / 60.0) / 60.0)
if exif_GPS[1] == 'S':
    latitude *= -1

longitude = str(longitude_degree + (longitude_minute + longitude_second / 60.0) / 60.0)
if exif_GPS[3] == 'W':
    longitude *= -1

webbrowser.open("https://www.google.com/maps/place/" + latitude + "+" + longitude)