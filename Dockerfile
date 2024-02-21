ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /competitive-ds-cource-prj
COPY poetry.lock pyproject.toml /competitive-ds-cource-prj/

RUN poetry install

CMD /bin/bash
