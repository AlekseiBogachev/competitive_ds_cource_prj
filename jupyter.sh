#!/bin/bash
./build.sh

docker run \
--rm \
--mount \
type=bind,src="$(pwd)",target=/dockeruser/comp_ds_prj \
-p 127.0.0.1:8080:8080 \
comp_ds_prj \
poetry run jupyter notebook \
--ip 0.0.0.0 \
--port 8080 \
--no-browser