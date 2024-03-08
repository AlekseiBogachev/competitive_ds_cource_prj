ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}

RUN apt-get update -y && apt install curl libdigest-sha-perl libssl3 -y

ARG UNAME=runneruser
ARG UID=1001
ARG GID=1001
ARG GITUSER="Aleksei Bogachev"
ARG GITEMAIL="bogachev.aleksey.m@gmail.com"

RUN groupadd  --gid $UID $UNAME
RUN useradd -g $GID -m -s /bin/bash -u $UID $UNAME


RUN mkdir /home/$UNAME/actions-runner 
WORKDIR /home/$UNAME/actions-runner

RUN curl -o actions-runner-linux-x64-2.314.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.314.1/actions-runner-linux-x64-2.314.1.tar.gz
RUN echo "6c726a118bbe02cd32e222f890e1e476567bf299353a96886ba75b423c1137b5  actions-runner-linux-x64-2.314.1.tar.gz" | shasum -a 256 -c
RUN tar xzf ./actions-runner-linux-x64-2.314.1.tar.gz

RUN chown -R $UNAME /home/$UNAME

RUN ./bin/installdependencies.sh


USER $UNAME

RUN git config --global user.name $GITUSER
RUN git config --global user.email $GITEMAIL

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/home/$UNAME/.local/bin:/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"


WORKDIR /home/$UNAME/comp_ds_prj

RUN poetry config installer.max-workers 10

COPY poetry.lock pyproject.toml /home/$UNAME/comp_ds_prj/
RUN poetry install --no-root


WORKDIR /home/$UNAME/actions-runner

RUN --mount=type=secret,id=token,uid=$UID \
    ./config.sh \
    --replace \
    --unattended \
    --name ubuntu-ds-runner \
    --labels ubuntu,ds,no-gpu \
    # --ephemeral \
    --url https://github.com/AlekseiBogachev/competitive_ds_cource_prj \
    --token $(cat /run/secrets/token)

CMD ./run.sh
