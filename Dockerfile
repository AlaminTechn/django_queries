FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./entrypoint.sh .

COPY . .

RUN chmod +x ./entrypoint.sh

EXPOSE 8001

ENTRYPOINT ["/entrypoint.sh"]

#CMD ["python", "run""]
#ENTRYPOINT [ "sh", "/entrypoin.sh" ]
