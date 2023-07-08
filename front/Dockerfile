FROM python:3.11.4-slim-bookworm

ENV DIRPATH=/workspace/front

WORKDIR $DIRPATH
COPY ./requirements.txt $DIRPATH/requirements.txt
RUN pip install --no-cache-dir --upgrade -r $DIRPATH/requirements.txt
COPY ./app $DIRPATH/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]