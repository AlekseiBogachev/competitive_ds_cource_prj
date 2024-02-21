#!/bin/bash
docker build -t py_poetry .
docker run --rm -it --mount type=bind,src="$(pwd)",target=/project py_poetry