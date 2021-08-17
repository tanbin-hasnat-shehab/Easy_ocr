import easyocr as ocr
reader=ocr.Reader(['en','bn'])
results=reader.readtext('mask.png')
text=''
for result in results:
	text+=result[1] + '\n'
print(text)