import qrcode

# URL to encode
url = "https://shakiraaaaaa.github.io/Asthma-guide-for-parents/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("asthma_guide_for_parents_qr.png")

print("QR code generated and saved as 'asthma_guide_qr.png'")
