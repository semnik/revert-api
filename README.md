revert-api
============


Установка
============
Для установки необходимо:
* [docker](https://docs.docker.com/install/)
* [docker-compose](https://docs.docker.com/compose/install/)





Запуск
============



Запуск сервиса:
```sh
docker-compose up -d
```

Остановка сервиса:
```sh
docker-compose down
```




Использование сервиса
============
Логи находятся в папке logs


В целях повышение производительности можно увеличить количество gunicorn workers 

Пример использования сервиса:
```sh
>>>  curl -X POST http://localhost:8080/revert -H 'Content-Type: application/json' -d '{"text": "abc 123"}'
{"response": "321 cba"}

```

Новый Docker образ можно создать командой
```sh
docker build -t semnik/revert-api .