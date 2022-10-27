az aks create -g k8sforbeginners-rg -n k8sforbeginners --enable-aad --enable-azure-rbac
az aks get-credentials -g k8sforbeginners-rg -n k8sforbeginners-aks-aad
AKS_ID=$(az aks show -g k8sforbeginners-rg -n k8sforbeginners  --query '[].id' -o tsv)
 az role assignment create --role "Azure Kubernetes Service RBAC Admin" --assignee 68df84cf-7bf5-4881-a23d-1ccd310b57de --scope $AKS_ID
