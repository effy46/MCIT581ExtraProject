# %pip install easyocr
# %pip install numpy==1.24.1
import easyocr

reader = easyocr.Reader(['ja'])

result = reader.readtext('other_test.png', paragraph=True)

for i in result:
    word = i[1]
    print(word)