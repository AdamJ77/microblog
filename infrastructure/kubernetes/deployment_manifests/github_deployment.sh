#!/bin/bash
set -x

K8S_PATH=infrastructure/kubernetes/deployment_manifests

kubectl apply -f $K8S_PATH/backend-deployment.yml 
kubectl apply -f $K8S_PATH/frontend-deployment.yml

<<<<<<< Updated upstream

NGINX_EXTERNAL_IP=$(kubectl get services nginx-service -o=jsonpath='{.status.loadBalancer.ingress[0].ip}')
kubectl set env deployment/frontend-deployment REACT_APP_SERVER_URL="http://${NGINX_EXTERNAL_IP}/api"
=======
# NGINX_EXTERNAL_IP=$(kubectl get services nginx-service -o=jsonpath='{.status.loadBalancer.ingress[0].ip}')
# kubectl set env deployment/frontend-deployment REACT_APP_SERVER_URL="http://${NGINX_EXTERNAL_IP}/api"
>>>>>>> Stashed changes
