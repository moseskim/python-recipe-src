import logging

# 핸들러를 생성한다
std_handler = logging.StreamHandler()
file_handler = logging.FileHandler("tmp.log")

# 포맷, 로그 레벨, 핸들러를 설정한다
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG,
                    handlers=[std_handler, file_handler])

logger = logging.getLogger(__name__)
logger.debug("디버그 출력")
logger.info("정보 출력")
logger.warning("경고 발생!")
logger.error("에러 발생!!")

