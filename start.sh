#!/bin/bash
docker build -t py_poetry .
docker run --rm -it --mount type=bind,src="$(pwd)",target=/competitive-ds-cource-prj py_poetry $@