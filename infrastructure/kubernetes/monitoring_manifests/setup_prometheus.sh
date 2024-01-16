#/bin/bash
set -exuo

# Set kubectl context to Microblog AKS
# az aks get-credentials --resource-group Microblog1 --name aks-Microblog1

# Check if K8s package manager - Helm is installed
if ! command -v helm &>/dev/null; then
    curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
    chmod 700 get_helm.sh
    ./get_helm.sh
fi

# Add Helm repo for Prometheus
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

# Install Helm Chart in monitoring namespace (including Grafana)
helm install prometheus \
  prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace

# Check monitoring stack
kubectl get all -n monitoring
