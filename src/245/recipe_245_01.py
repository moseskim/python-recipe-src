# 실행할 떄는 img 디렉터리 아래의 pillow_sample.jpg를 스크립트와 같은 디렉터리에 배치한 뒤 실행합니다.

from PIL import Image

image = Image.open('pillow_sample_1.jpg')
image2 = image.transpose(Image.FLIP_TOP_BOTTOM)
image2.show()
image2.save('new_sample.jpg')
