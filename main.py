# basic_qrcode.py

import segno

qrcode = segno.make_qr("https://youtu.be/dQw4w9WgXcQ?si=dWfFeA4x6RdyzZFp", error='H')
qrcode.save("basic_qrcode.png",
            scale=6,
            )

from PIL import Image

# Open the logo image
logo = Image.open("NSSLOGO.png")

# Resize the logo
basewidth = 100
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.LANCZOS)

# Save the resized logo
logo.save("resized_logo.png")


qr_img = Image.open("basic_qrcode.png").convert("RGBA")
logo = Image.open("resized_logo.png").convert("RGBA")

# Calculate the position (center of the QR code)
qr_width, qr_height = qr_img.size
logo_width, logo_height = logo.size
logo_position = ((qr_width - logo_width) // 2, (qr_height - logo_height) // 2)

qr_img.paste(logo, logo_position, logo)

qr_img.save("qrwithlogo.png")