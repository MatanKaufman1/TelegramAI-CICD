FROM python:3.8.12-slim-buster
WORKDIR /app
ARG CONFIG_FILE
COPY ${CONFIG_FILE} /qa_bot/config-test.json
ENV ENV test
COPY . .
RUN pip install -r qa/requirements.txt

CMD ["python3", "-m", "bot.test", "bot.app"]