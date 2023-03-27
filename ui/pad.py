# python -m pip install paddlepaddle -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install "paddleocr>=2.0.1"
#pip install opencv-python==4.5.5.64
#astor-0.8.1 opt-einsum-3.3.0 paddle-bfloat-0.1.7 paddlepaddle-2.4.2 protobuf-3.20.0

#https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.6/doc/doc_en/quickstart_en.md
from paddleocr import PaddleOCR,draw_ocr
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(use_angle_cls=True, lang='japan') # need to run only once to download and load model into memory
img_path = 'other_test.png'
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)

# import fitz
# from PIL import Image
# import cv2
# import numpy as np
# imgs = []
# with fitz.open(img_path) as pdf:
#     for pg in range(0, pdf.page_count):
#         page = pdf[pg]
#         mat = fitz.Matrix(2, 2)
#         pm = page.get_pixmap(matrix=mat, alpha=False)
#         # if width or height > 2000 pixels, don't enlarge the image
#         if pm.width > 2000 or pm.height > 2000:
#             pm = page.getPixmap(matrix=fitz.Matrix(1, 1), alpha=False)
#
#         img = Image.frombytes("RGB", [pm.width, pm.height], pm.samples)
#         img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
#         imgs.append(img)
# for idx in range(len(result)):
#     res = result[idx]
#     image = imgs[idx]
#     boxes = [line[0] for line in res]
#     txts = [line[1][0] for line in res]
#     scores = [line[1][1] for line in res]
#     im_show = draw_ocr(image, boxes, txts, scores, font_path='doc/fonts/simfang.ttf')
#     im_show = Image.fromarray(im_show)
#     im_show.save('result_page_{}.jpg'.format(idx))