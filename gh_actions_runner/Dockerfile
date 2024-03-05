FROM ubuntu:22.04

RUN apt-get update -y && apt install curl libdigest-sha-perl -y

RUN useradd -m -s /bin/bash -u 1200 runneruser

RUN mkdir /home/runneruser/actions-runner 
WORKDIR /home/runneruser/actions-runner

RUN curl -o actions-runner-linux-x64-2.314.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.314.1/actions-runner-linux-x64-2.314.1.tar.gz
RUN echo "6c726a118bbe02cd32e222f890e1e476567bf299353a96886ba75b423c1137b5  actions-runner-linux-x64-2.314.1.tar.gz" | shasum -a 256 -c
RUN tar xzf ./actions-runner-linux-x64-2.314.1.tar.gz

RUN chown -R runneruser /home/runneruser/actions-runner

RUN ./bin/installdependencies.sh

USER runneruser

RUN --mount=type=secret,id=token,uid=1200 ./config.sh --replace --unattended --url https://github.com/AlekseiBogachev/competitive_ds_cource_prj --token $(cat /run/secrets/token) -y

CMD /bin/bash -c ./run.sh