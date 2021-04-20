import qrcode
author="@Author: John Jayson B. De Leon"
github="@Github: savjaylade84"
print(author + "\n" + github,"\n")
url=input("[ Enter Url ]: ")
file_name=input("\n[Enter Qr Code Name:] ")
image = qrcode.make(url)
image.save(file_name+".png","PNG")
print("\n[Saving QR Code...]@("+file_name+".png)\n[ Done... ]","\n")