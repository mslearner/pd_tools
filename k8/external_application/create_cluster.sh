#!/bin/bash
set -x

read -n 1
az group create --name az_cluster --location eastus  --tags 'Owner=pdewan'
  
read -n 1
az aks create --resource-group az_cluster --name my-aks-cluster --node-count 2 --generate-ssh-keys --enable-addons http_application_routing --node-vm-size Standard_DS2_v2  --tags 'Owner=pdewan'
 

read -n 1
az aks get-credentials --resource-group az_cluster --name my-aks-cluster
 


read -n 1
az aks show -g az_cluster -n my-aks-cluster \
 --query addonProfiles.httpApplicationRouting.config.HTTPApplicationRoutingZoneName -o table


read -n 1
kubectl get deploy,svc,ing
