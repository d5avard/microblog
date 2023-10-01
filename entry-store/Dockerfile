FROM python:3.11.4-bookworm as build

ENV APPNAME=entry-store
ENV WORKSPACEPATH=/workspace/${APPNAME}
WORKDIR $WORKSPACEPATH
COPY ./requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

FROM build
WORKDIR $WORKSPACEPATH
COPY ./app ./
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
