#!/bin/bash
set -x
echo $CLUSTER_GROUP_NAME
az group delete --name ${CLUSTER_GROUP_NAME} --yes --no-wait

