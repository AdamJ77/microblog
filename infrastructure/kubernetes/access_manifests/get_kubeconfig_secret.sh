#!/bin/bash

K8S_PATH=infrastructure/kubernetes/access_manifests

kubectl apply -f $K8S_PATH/service-account.yml
kubectl apply -f $K8S_PATH/role.yml
kubectl apply -f $K8S_PATH/role-binding.yml

# Create K8s secret for SA
SA_SECRET=$(kubectl get secret $(kubectl get serviceaccount deploy-sa -o jsonpath='{.secrets[0].name}') -o jsonpath='{.data.token}' | base64 --decode)

kubectl create secret generic deploy-sa-secret --from-literal=token=$SA_SECRET | base64

echo $SA_SECRET