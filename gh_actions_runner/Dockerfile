FROM comp_ds_prj_base

USER root

RUN apt-get update -y && apt install curl libdigest-sha-perl libssl3 -y

RUN curl -o actions-runner-linux-x64-2.314.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.314.1/actions-runner-linux-x64-2.314.1.tar.gz
RUN echo "6c726a118bbe02cd32e222f890e1e476567bf299353a96886ba75b423c1137b5  actions-runner-linux-x64-2.314.1.tar.gz" | shasum -a 256 -c
RUN tar xzf ./actions-runner-linux-x64-2.314.1.tar.gz
RUN ./bin/installdependencies.sh

ARG UNAME=dockeruser
RUN chown -R $UNAME /$UNAME
USER $UNAME

COPY poetry.loc[k] pyproject.toml ./
RUN poetry install --no-root

CMD /bin/bash
