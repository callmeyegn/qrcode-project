import qrcode

# Generate the QR code
img = qrcode.make('https://www.wikipedia.org')

# Save it as an image file
img.save('simple_qr.png')