#!/bin/bash

K8S_PATH=infrastructure/kubernetes/access_manifests

kubectl apply -f $K8S_PATH/service-account.yml --user=deploy-sa
kubectl apply -f $K8S_PATH/role.yml --user=deploy-sa
kubectl apply -f $K8S_PATH/role-binding.yml --user=deploy-sa

# Create K8s secret for SA
SA_SECRET=$(kubectl get secret $(kubectl get serviceaccount deploy-sa -o jsonpath='{.secrets[0].name}') -o jsonpath='{.data.token}') # | base64 --decode)

kubectl create secret generic deploy-sa-secret --from-literal=token=$SA_SECRET

echo "::set-output name=SA_SECRET_BASE64::$(echo -n $SA_SECRET | base64)"

echo $SA_SECRET

kubectl config set-credentials deploy-sa --token=$SA_SECRET
kubectl config set-context deploy-context --cluster=aks-Microblog1 --user=deploy-sa
kubectl config use-context deploy-context
kubectl config view --minify --flatten > kubeconfig.yaml

# Output the base64-encoded kubeconfig for GitHub Actions
KUBE_CONFIG_BASE64=$(cat kubeconfig.yaml | base64)
