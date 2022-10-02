# from PIL import Image
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#
# text = pytesseract.image_to_string(Image.open('wordcloudManiTejas.png'), lang="eng")
# print(text)

# # text to image
#
# import Image
# import ImageDraw
# import ImageFont
#
#
# def getSize(txt, font):
#     testImg = Image.new('RGB', (1, 1))
#     testDraw = ImageDraw.Draw(testImg)
#     return testDraw.textsize(txt, font)
#
#
# if __name__ == '__main__':
#     fontname = "Arial.ttf"
#     fontsize = 11
#     text = "example@gmail.com"
#
#     colorText = "black"
#     colorOutline = "red"
#     colorBackground = "white"
#
#     font = ImageFont.truetype(fontname, fontsize)
#     width, height = getSize(text, font)
#     img = Image.new('RGB', (width + 4, height + 4), colorBackground)
#     d = ImageDraw.Draw(img)
#     d.text((2, height / 2), text, fill=colorText, font=font)
#     d.rectangle((0, 0, width + 3, height + 3), outline=colorOutline)
#
#     img.save("image.png")


# # convert extension of image
#
# import aspose.words as aw
#
# doc = aw.Document()
# builder = aw.DocumentBuilder(doc)
#
# builder.insert_image("wallpaper.JPG")
#
# doc.save("Output.pdf")
#
# # { docx , pdf , md , html , txt , doc , dot , docm , dotx , dotm , rtf , epub ps , pcl , mhtml , xhtml , odt ott ,\
# # xps , png}
