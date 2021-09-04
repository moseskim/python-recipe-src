import logging

format_str = '%(asctime)s - %(process)d - %(thread)d - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=format_str, level=logging.INFO)

logger = logging.getLogger(__name__)
logger.debug("디버그 출력")
logger.info("정보 출력")
logger.warning("경고 발생!")
logger.error("에러 발생!!")
