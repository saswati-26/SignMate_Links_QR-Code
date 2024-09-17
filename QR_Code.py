import qrcode

webpage_url = "./localhost_link.txt"

qr = qrcode.QRCode(

    version = 1,  # QR code version
    error_correction = qrcode.constants.ERROR_CORRECT_L,  # Error correction
    box_size = 10,  # Box Size
    border = 4,  # Border size

)
qr.add_data(webpage_url)
qr.make(fit = True)

img = qr.make_image(fill = 'black', back_color = 'white')

img.save("QR_Code.png")

print("QR code generated and saved as QR_Code.png")