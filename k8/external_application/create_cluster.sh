#!/bin/bash
set -x
echo CLUSTER_NAME=${CLUSTER_NAME}
echo CLUSTER_GROUP_NAME=${CLUSTER_GROUP_NAME}
export CLUSTER_REGION=westus

read -n 1
az group create --name ${CLUSTER_GROUP_NAME} --location ${CLUSTER_REGION}  --tags 'Owner=pdewan'
  
read -n 1
az aks create --resource-group ${CLUSTER_GROUP_NAME} --name ${CLUSTER_NAME} --node-count 2 \
--generate-ssh-keys \
#--enable-addons  http_application_routing \
#--node-vm-size Standard_DS2_v2  \
--tags 'Owner=pdewan'
 

read -n 1
az aks get-credentials --resource-group ${CLUSTER_GROUP_NAME} --name ${CLUSTER_NAME}
 


read -n 1
#az aks show -g az_cluster -n my-aks-cluster \
# --query addonProfiles.httpApplicationRouting.config.HTTPApplicationRoutingZoneName -o table


read -n 1
#kubectl get deploy,svc,ing
