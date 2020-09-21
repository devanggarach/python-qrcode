import pyqrcode 
import png 
from pyqrcode import QRCode 
from  PIL import Image, ImageDraw, ImageFont #Qr generate
import cv2

def QRSave(**kwargs):
    pqrcode=kwargs.get("pqrcode",None)
    pname=kwargs.get("pname",None)
    fname = f'{pname}_{pqrcode}.png'
    mrp=kwargs.get("mrp",None)
    spprice1=kwargs.get("spprice",None)
    expiredate=kwargs.get("expiredate",None)
    mfdate=kwargs.get("manfdate",None)
    businessname=kwargs.get("businessname",None)
    

    url = pyqrcode.create(pqrcode)
    url.png(fname, scale = 4)

    img=Image.open(fname,'r')
    img_w, img_h = img.size
    background = Image.new('RGBA', (144, 144), (255, 255, 255, 255))#244
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)

    background.paste(img, offset)

    draw        = ImageDraw.Draw(background)

    MRPfont     = ImageFont.truetype("Saira-Bold.ttf",7) #12
    Productfont = ImageFont.truetype("Saira-Bold.ttf",11)#18
    SPPricefont = ImageFont.truetype("Saira-Bold.ttf",12)#22
    productcodefont  = ImageFont.truetype("Saira-Bold.ttf",8)#12

    w,h  =MRPfont.getsize(mrp)
    w1,h1=Productfont.getsize(pname)
    w2,h2=SPPricefont.getsize(spprice1)

    draw.text(((bg_w-w)/2, 0),mrp,(0,0,0),font=MRPfont)
    draw.text(((bg_w-w1)/2, 5),pname,(0,0,0),font=Productfont)#10

    draw.rectangle((0,bg_h-h2,bg_w,bg_h), fill='black')
    draw.text(((bg_w-w2) // 2, bg_h-(h2+1)), spprice1, (255,255,255), font=SPPricefont)#5
    
    background.save(fname)

    img = cv2.imread(fname)
    img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(fname, img_rotate_90_clockwise)

    img = Image.open(fname, 'r')
    img_w, img_h = img.size
    draw = ImageDraw.Draw(img)
    BusinessNamefont = ImageFont.truetype("Saira-Bold.ttf",17)#22
    ExpireDatefont   = ImageFont.truetype("Saira-Bold.ttf",7)#11
    MFDatefont   = ImageFont.truetype("Saira-Bold.ttf",7)#11
    w,h  =BusinessNamefont.getsize(businessname)
    w2,h2=productcodefont.getsize(pqrcode)
    w3,h3=ExpireDatefont.getsize(expiredate)
    # w4,h4=MFDatefont.getsize(mfdate)

    draw.text((((bg_w-w)/2)+0, -3),businessname,(0,0,0),font=BusinessNamefont)#12
    draw.text((20, bg_h-(h2+1)*2),pqrcode,(0,0,0),font=productcodefont)#3  
    draw.text((20+w3+4, bg_h-(h3+2)),expiredate,(0,0,0),font=ExpireDatefont)#3
    draw.text((20, bg_h-(h3+2)),mfdate,(0,0,0),font=MFDatefont)#3

    img.save(fname)

    img = cv2.imread(fname)
    img_rotate_90_counterclockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imwrite(fname, img_rotate_90_counterclockwise)

QRSave(pqrcode="21UA4567X01",pname="Mango Keshar 1Pcs.",mrp="MRP Rs. 26.09/-",spprice="Sp. Rs. 20.99/-",expiredate="Exp. 12-12-2020",manfdate="Mfd. 11-06-2020",businessname="MegaMart")