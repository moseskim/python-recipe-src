# 실행할 떄는 img 디렉터리 아래의 pillow_sample.jpg를 스크립트와 같은 디렉터리에 배치한 뒤 실행합니다.
# 또한 다음 URL에서 이미지를 다운로드해 현재 디렉터리에 python-logo.png로 저장합니다.
# https://www.python.org/static/community_logos/python-logo-master-v3-TM.png

from PIL import Image

image = Image.open("pillow_sample.jpg")
logo = Image.open("python-logo.png")
image.paste(logo, (100, 100))
image.save("pillow_paste.jpg")
