#!/bin/bash
docker build -t comp_ds_prj --progress=plain . 2>&1 | tee ./logs/docker_build.log
docker run --rm -it --mount type=bind,src="$(pwd)",target=/comp_ds_prj comp_ds_prj $@