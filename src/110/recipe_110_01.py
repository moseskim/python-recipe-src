import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.debug("디버그 출력")
logger.info("정보 출력")
logger.warning("경고 발생!")
logger.error("에러 발생!!")
