#!/bin/bash
set -x

K8S_PATH=infrastructure/kubernetes/deployment_manifests

kubectl apply -f $K8S_PATH/backend-deployment.yml 
kubectl apply -f $K8S_PATH/frontend-deployment.yml