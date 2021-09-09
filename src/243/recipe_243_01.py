# 스크립트를 실행할 때는 다음 URL에서 이미지를 다운로드 하고, 스크립트와 같은 디렉터리에 python-logo.png로 배치합니다
# https://legacy.python.org/community/logos/python-powered-h-50x65.png

from PIL import Image

image = Image.open('python-logo.png')
# 파일 포맷 얻기
print(image.format)

# 픽셀 형식 얻기 ("1", "L", "RGB", "CMYK" 등)
print(image.mode)

# 이미지 크기 얻기
print(image.size)
