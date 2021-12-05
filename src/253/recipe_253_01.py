# 실행할 떄는 img 디렉터리 아래의 pillow_sample.jpg를 스크립트와 같은 디렉터리에 배치한 뒤 실행합니다.

from PIL import Image
from PIL.ExifTags import TAGS

image = Image.open("pillow_sample.jpg")
exif = image._getexif()
for id, value in exif.items():
    print(id, TAGS.get(id), value)
