#!/bin/bash
DOCKER_BUILDKIT=1 \
docker build \
--tag self-hosted-runner \
--progress=plain \
--no-cache \
--secret id=token,src=.secret_token \
. \
2>&1 | tee ./docker_build.log

docker run \
--rm \
-it \
self-hosted-runner

docker image rm -f self-hosted-runner