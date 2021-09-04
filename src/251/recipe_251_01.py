# 실행할 떄는 img 디렉터리 아래의 pillow_sample.jog를 스크립트와 같은 디렉터리에 배치한 뒤 실행합니다.
# 폰트 경로는 사용하는 환경에 맞게 변경합니다.

from PIL import Image, ImageFont, ImageDraw

image= Image.open("pillow_sample.jpg")
text = "Python Recipe"
color = (255, 255, 255)
font_size = 128
font = ImageFont.truetype(r"C:\Windows\Fonts\msgothic.ttc", font_size)
draw = ImageDraw.Draw(image)
draw.text((100, 100), text, font=font, fill=color)
image.save("pillow_text.jpg")
