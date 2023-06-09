FROM python:3.8

RUN mkdir /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock main.py /app/
WORKDIR /app

# This could be cached using workarounds in https://github.com/python-poetry/poetry/issues/1301
# Also it ideally would be --no-dev but that would require more stuff to run unit tests in here.
RUN poetry install

ENTRYPOINT [ "poetry", "run", "python", "main.py" ]