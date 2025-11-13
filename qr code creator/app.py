import qrcode

def create_qr(data, filename="qrcode.png"):
    qr = qrcode.make(data)
    qr.save(filename)
    print(f"QR Code saved as {filename}")

create_qr("https://www.forgedinfire.us/")
