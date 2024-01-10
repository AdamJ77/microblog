#!/bin/bash
set -x

resourceGroup=Microblog1
nsgName=mongodb-nsg

K8S_PATH=infrastructure/kubernetes/deployment_manifests

# SETUP BACKEND
kubectl apply -f $K8S_PATH/backend-deployment.yml 
kubectl apply -f $K8S_PATH/backend-service.yml

# SETUP FRONTEND
kubectl apply -f $K8S_PATH/frontend-deployment.yml
kubectl apply -f $K8S_PATH/frontend-service.yml

# SETUP NGINX
kubectl apply -f $K8S_PATH/nginx-deployment.yml 
kubectl apply -f $K8S_PATH/nginx-service.yml

sleep 20

# Fetch the external IP of the Nginx service
NGINX_EXTERNAL_IP=$(kubectl get services nginx-service -o=jsonpath='{.status.loadBalancer.ingress[0].ip}')

# Add Inbound rule to MongoDB
az network nsg rule create \
  --resource-group $resourceGroup \
  --nsg-name $nsgName \
  --name "Allow27017" \
  --priority 1000 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-address-prefixes $NGINX_EXTERNAL_IP \
  --source-port-ranges '*' \
  --destination-address-prefixes '*' \
  --destination-port-ranges 27017

echo $NGINX_EXTERNAL_IP

# CONFIGURE REST IP ADDRESS IN FRONTEND
kubectl set env deployment/frontend-deployment REACT_APP_SERVER_URL="http://${NGINX_EXTERNAL_IP}/api"
