import easyocr
reader = easyocr.Reader(['ch_sim','en'])
result = reader.readtext('examples\easyocr_framework.jpeg')
print(result)