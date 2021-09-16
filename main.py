import qrcode
import cv2
import os
import subprocess
import sys
import json

# get desktop directory
if sys.platform == "win32":
    command = r'reg query "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" /v "Desktop"'
    result = subprocess.run(command, stdout=subprocess.PIPE, text = True)
    desktop = result.stdout.splitlines()[2].split()[2]
else:
    desktop = os.path.expanduser("~/Desktop")

# set result location directory on desktop
res_loc = os.path.join(desktop, 'qrcode')

# make the directory if it does not exist
if not res_loc:
    os.makedirs(res_loc)

# ask user for text/url to generate a qrcode of
print('please enter text or url to generate a qrcode of:')
input = input()

# generate the qrcode
img = qrcode.make(input)

# get count in the count.json file so that user can generate multiple qrcodes without the qrcodes overwriting every time.
input_file=open('count.json', 'r')
json_decode=json.load(input_file)
count = json_decode['count']

# save the qrcode
img_save = os.path.join(res_loc, f'result{count}.jpg')
img.save(img_save)

# increments the count and saves it in json file
count = count + 1
data = {
    'count': count,
}
with open('count.json', 'w') as f:
    json.dump(data, f)

# display the qrcode
image = cv2.imread(img_save)
cv2.imshow('qr code', image)
cv2.waitKey(0)