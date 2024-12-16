# Запуск локально
1. Скачать проект на ПК любым удобным способом
2. Открыть терминал и перейти в директорию проекта
3. Создать [виртуальное окружение](https://www.studytonight.com/post/python-virtual-environment-setup-on-mac-osx-easiest-way) `python3 -m venv venv` и активировать его `source venv/bin/activate`
4. Установить все зависимости проекта `pip install -r requirements.txt`
5. Создать файл виртуального окружения `.env` и заполнить его ключами.
Переменные, которые необходимо прописать и заполнить:
```
BOT_TOKEN=

DATABASE_HOST=
DATABASE_PORT=
DATABASE_NAME=
DATABASE_USERNAME=
DATABASE_PASSWORD=

```
6. Написать в терминале `python3 main.py` для запуска*
>Примечание: для корректной работы Chat-GPT в России необходимо запустить VPN

Для удобства и запуска можно использовать [докер контейнер](https://hub.docker.com/repository/docker/limon4egtop/light_sno_helper/general)

## Cборка собственного докер контейнера
Для сборки и отправки своего контейнера в DockerHub рекомендуется использовать следующую команду:
```
docker buildx build --platform linux/amd64,linux/arm64 -t limon4egtop/light_sno_helper --push .
```

# Запуск на сервере
1. Для запуска последней версии бота нам необходимо скачать его из [докерхаба](https://hub.docker.com/repository/docker/limon4egtop/light_sno_helper/general)
```
docker pull limon4egtop/light_sno_helper
```
2. Далее мы можем проверить скачался ли наш образ
```
docker images
```
3. Смотрим какой контейнер запущен сейчас
```
docker ps
```
5. Останавливаем запущенный контейнер
```
docker stop *contaner id*
```
7. Запускаем скаченный контейнер и обязательно указываем переменные окружения и название контейнера
```
docker run -d \
    --name light_sno_helper \
    -e BOT_TOKEN="" \
    -e DATABASE_HOST="" \
    -e DATABASE_PORT="" \
    -e DATABASE_NAME="" \
    -e DATABASE_USERNAME="" \
    -e DATABASE_PASSWORD="" \
    limon4egtop/light_sno_helper
```
