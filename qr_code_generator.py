import qrcode

website =input("Enter the link: ")

qr = qrcode.QRCode(version = 1, box_size = 5, border= 5)

qr.add_data(website) #the qr data must be the website link
qr.make() #make qr code

fill = input("Insert the rgb code for the fill color: ")
back = input("Insert the rgb code for the background color: ")

image = qr.make_image(fill_color= fill, back_color= back)

name= input("Choose the image's file name: ")

image.save(f"{name}.png")