#!/bin/bash
docker exec -it comp_ds_runner ./config.sh remove --token $(cat .secret_token)
docker image rm -f self-hosted-runner
