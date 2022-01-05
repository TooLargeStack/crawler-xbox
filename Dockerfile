FROM python:3.8

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
RUN poetry install

CMD "poetry run python crawler"