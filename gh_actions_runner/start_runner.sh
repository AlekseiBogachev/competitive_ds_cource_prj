#!/bin/bash
docker run \
--rm \
-it \
--name comp_ds_runner \
self-hosted-runner /bin/bash -c "\
./config.sh \
--replace \
--unattended \
--name ubuntu-ds-runner \
--labels ubuntu,ds,no-gpu \
--url https://github.com/AlekseiBogachev/competitive_ds_cource_prj \
--token $(cat ./gh_actions_runner/.secret_token) && \
./run.sh"