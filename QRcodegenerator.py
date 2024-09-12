import qrcode 
from PIL import Image

#Create a QRCode object
qr=qrcode.QRCode(
    version=15, #15 means the higher the version of the qrcode number the biggere the code image and the more comp;icated the picture
    box_size=10, #size ff the box where the qrcode will be displayed
    border=5 #it is the white part of the image --all four sides with the white colour
)
#Data to encode
data="https://www.linkedin.com/in/afia-pokuaa/"
#if you dont want to redirect and create for normal text then write text in quotes like a string

#Add data to QRCode
qr.add_data(data)
qr.make(fit=True)


#Create an image for the QRCode
img=qr.make_image(fill="black",back_color="white")

#Save image to the file
img.save("first.png")