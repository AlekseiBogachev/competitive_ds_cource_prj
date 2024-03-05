#!/bin/bash
./build.sh

docker run \
--rm \
-it \
--mount \
type=bind,src="$(pwd)",target=/dockeruser/comp_ds_prj \
comp_ds_prj \
$@
