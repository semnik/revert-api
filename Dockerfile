
FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN chmod +x entry_point.sh
RUN pip install -r requirements.txt
RUN mkdir -p /app/logs
EXPOSE 8080
ENTRYPOINT ["sh", "entry_point.sh"]