#!/bin/bash
docker build \
--build-arg UID=$(id -u) \
--build-arg GID=$(id -g) \
--build-arg GITUSER="$(git config user.name)" \
--build-arg GITEMAIL="$(git config user.email)" \
-t comp_ds_prj \
--progress=plain \
. \
2>&1 | tee ./logs/docker_build.log

docker run \
--rm \
-it \
--mount \
type=bind,src="$(pwd)",target=/dockeruser/comp_ds_prj \
comp_ds_prj \
$@
