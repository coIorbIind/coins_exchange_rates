FROM python:3.10.12

RUN mkdir "app/"

WORKDIR "app/"

COPY src/requirements.txt src/requirements.txt

RUN pip install -r src/requirements.txt

RUN mkdir logs

COPY src/ src/

COPY entrypoints/ entrypoints/

ENV PYTHONPATH "/app/src/coins_exchange_rates"

RUN chmod a+x entrypoints/*.sh

CMD entrypoints/app.sh
