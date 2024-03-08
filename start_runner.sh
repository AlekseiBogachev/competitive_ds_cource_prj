#!/bin/bash
DOCKER_BUILDKIT=1 \
docker build \
--tag self-hosted-runner \
--progress=plain \
--no-cache \
--secret id=token,src=./gh_actions_runner/.secret_token \
--file ./gh_actions_runner/Dockerfile \
. \
2>&1 | tee ./docker_build.log

docker run \
--rm \
-it \
--name comp_ds_runner \
self-hosted-runner
