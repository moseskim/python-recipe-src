# 실행할 떄는 img 디렉터리 아래의 pillow_sample.jpg를 스크립트와 같은 디렉터리에 배치한 뒤 실행합니다.

from PIL import Image

image = Image.open("pillow_sample.jpg")
new_image1 = image.transpose(Image.FLIP_LEFT_RIGHT)
new_image1.save("pillow_flip1.jpg")
new_image2 = image.transpose(Image.FLIP_TOP_BOTTOM)
new_image2.save("pillow_flip2.jpg")
