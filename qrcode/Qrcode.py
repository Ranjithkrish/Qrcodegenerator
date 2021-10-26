import qrcode
import image
rn = qrcode.QRCode(
    version=15,
    box_size=6,
    border=4
)
content="https://scontent.whatsapp.net/v/t61.25591-34/245469226_1212243505957047_8961976802414016189_n.apk/WhatsApp.apk?ccb=1-5&_nc_sid=4a4126&_nc_ohc=eVhNP_k16bMAX9YhRVl&_nc_ht=scontent.whatsapp.net&oh=d5304d0a92511ef485027c743be51697&oe=616B2EF8"
rn.add_data(content)
rn.make(fit=True)
pic= rn.make_image(fill="black",back_color = "white")
pic.save("qr.png")