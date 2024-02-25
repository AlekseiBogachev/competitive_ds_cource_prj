ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /comp_ds_prj

RUN poetry config installer.max-workers 10

COPY poetry.lock pyproject.toml /comp_ds_prj/
RUN poetry install --no-root

RUN git config --global user.name "Aleksei Bogachev"
RUN git config --global user.email "bogachev.aleksey.m@gmail.com"

CMD /bin/bash
