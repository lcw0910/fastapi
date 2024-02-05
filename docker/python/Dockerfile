FROM python:3.11

# 작업 디렉토리 설정
WORKDIR /app

# Create a user, so we aren't running as root
RUN adduser --disabled-password --gecos '' pyuser

# 의존성 파일 복사 및 설치
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install "pydevd-pycharm==233.13763.11"


USER pyuser

# Uvicorn 서버 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
