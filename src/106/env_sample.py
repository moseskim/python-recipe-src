import os

app_env = os.environ.get("APP_ENV")
if app_env == 'DEV':
    print("개발 환경에서 실행합니다.")
elif app_env == 'PROD':
    print("운영 환경에서 실행합니다")
else:
    print("적절한 환경 변수가 설정되어 있지 않습니다.")
