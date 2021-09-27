from exif import Image
import os

with open("20210725_161005.jpg", 'rb') as img_file:
	im = Image(img_file)
	
print("[-] Extraction........")

if im.has_exif:
	print(im.gps_longitude, im.gps_latitude)
else:
	print("[x] No Metadatas founds...")
	
os.system("pause")
