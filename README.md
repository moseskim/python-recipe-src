# 파이썬 코드 레시피 302 샘플 소스 코드

이 저장소에는 파이썬 코드 레시피 302에서 소개한 소스 코드(파이썬 스크립트) 및 참고 문헌 링크를 제공합니다.

## 폴더 구성과 실행 방법

이 저장소의 폴더는 다음과 같이 구성됩니다. `src` 폴더 아래 항목별로 폴더가 존재하며, 그 안에 `recipe_항목번호_연번.py` 형식으로 소스 코드가 저장되어 있습니다.

```
.
├───src
│    ├───001
│    │    ├─── recipe_001_01.py
│    │    └─── recipe_001_02.py
│    ├───002
│    ├───003
│    :
│    └───img
:
├───requirements.txt
└───README.md
```

각 항목 번호의 폴더가 현재 디렉터리인 상태에서 실행합니다. 예를 들어 윈도우 계열의 환경에서 현재 디렉터리가 루트 디렉토리일 때, 레시피 001의 코드는 다음 명령어로 실행할 수 있습니다.

```
cd src\001
python sample.py
```

일부 코드는 실행 전 별도의 준비가 필요할 수 있습니다.

* 경로나 파일을 다루는 코드에서는 책(또는 샘플)에서 설명하는 전제 조건에 맞춰 파일을 배치하고, 경로를 정리해야 합니다.
* 하드 코딩된 경로는 윈도우 운영체제 기준입니다. 유닉스 계열의 운영 체제를 이용할 때는 사용하는 환경에 맞춰 적절하게 수정하기 바랍니다.

몇몇 샘플 코드를 실행할 때는 서드파티 라이브러리가 필요합니다. 개별 설치 또는 `requirements.txt`를 이용해 `pip` 명령어로 일괄 설치하기 바랍니다.

## 면책 사항

저자(옮긴이)의 환경에서 샘플 코드의 실행에 이상이 발생하지 않음을 확인했으나, 만일 무언가의 이유로 장애가 발생하는 경우에 관해서는 어떠한 보증도 하지 않습니다. 본인의 판단에 따라 이용하기 바랍니다.

## 저작권

샘플 파일은 저작권법상의 보호를 받습니다. 수록된 파일의 일부 또는 전부에 관해서는 어떤 형태로의 무단 복사, 복제, 재배포를 금합니다.

