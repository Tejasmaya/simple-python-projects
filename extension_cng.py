# convert pdf to docx
import aspose.words as aw

doc = aw.Document("C:\\Users\\Tejasmaya Sitha\\OneDrive\\Desktop\\Tejasmaya_Aadhar.pdf")  # give path of the file
doc.save("C:\\Users\\Tejasmaya Sitha\\OneDrive\\Desktop\\Output.docx")  # give a name to the output file

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
