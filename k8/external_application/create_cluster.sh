#!/bin/bash
set -x

read -n 1
az group create --name az_cluster --location westus
  
read -n 1
az aks create --resource-group az_cluster --name my-aks-cluster --node-count 3 --generate-ssh-keys --enable-addons http_application_routing
 

read -n 1
az aks get-credentials --resource-group az_cluster --name my-aks-cluster
 

read -n 1
kubectl label pods nginx-pod owner-

read -n 1
az aks show -g az_cluster -n my-aks-cluster \
 --query addonProfiles.httpApplicationRouting.config.HTTPApplicationRoutingZoneName -o table


read -n 1
kubectl get deploy,svc,ing
