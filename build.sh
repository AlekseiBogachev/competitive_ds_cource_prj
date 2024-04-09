#!/bin/bash

echo "Сборка базового образа" | tee ./logs/docker_build.log

docker build \
--build-arg GITUSER="$(git config user.name)" \
--build-arg GITEMAIL="$(git config user.email)" \
--build-arg REPO="AlekseiBogachev/competitive_ds_cource_prj.git" \
-t comp_ds_prj_base \
--progress=plain \
. \
2>&1 | tee -a ./logs/docker_build.log

echo "Сборка образа среды разработки" | tee ./logs/docker_build.log

BUILDKIT_PROGRESS=plain \
docker build \
-f Dockerfile_dev_env \
-t comp_ds_prj_dev \
--progress=plain \
--no-cache \
--secret id=pat,src=.dev_env_pat \
. \
2>&1 | tee -a ./logs/docker_build.log
