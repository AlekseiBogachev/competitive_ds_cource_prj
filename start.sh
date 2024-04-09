#!/bin/bash
./build.sh

docker run \
--rm \
-it \
comp_ds_prj_dev \
$@
