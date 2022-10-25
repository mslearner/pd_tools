#!/bin/bash 
set -x
echo "I'm just a dummy config file" >> $HOME/configfile.txt
read -n 1
kubectl create cm my-sixth-configmap --from-literal=color=yellow --from-file=$HOME/configfile.txt
read -n 1

kubectl create -f nginx-pod-with-configmap-volume.yaml
read -n 1

kubectl exec Pods/nginx-pod-with-configmap-volume -- ls /etc/conf
read -n 1



