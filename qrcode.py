import pyqrcode
import png


def qrcodegenerator():
    qr = pyqrcode.create(input())
    qr.png("qrcode.png", scale=6)
    print("QR Code is generated.")


if __name__ == '__main__':
    qrcodegenerator()
