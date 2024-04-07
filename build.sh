#!/bin/bash

echo "Сборка базового образа" | tee ./logs/docker_build.log

docker build \
--build-arg GITUSER="$(git config user.name)" \
--build-arg GITEMAIL="$(git config user.email)" \
-t comp_ds_prj_base \
--progress=plain \
. \
2>&1 | tee -a ./logs/docker_build.log

echo "Сборка образа среды разработки" | tee ./logs/docker_build.log

docker build \
-f Dockerfile_dev_env \
-t comp_ds_prj_dev \
--progress=plain \
. \
2>&1 | tee -a ./logs/docker_build.log
