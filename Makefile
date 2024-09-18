install:
    poetry install

dev:
    poetry run flask --app page_analyzer:app run

start:
    PORT ?= 8000
    poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app