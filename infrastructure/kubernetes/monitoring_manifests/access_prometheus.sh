#!/bin/bash

# Expose Prometheus UI (localhost:4001)
kubectl port-forward svc/prometheus-kube-prometheus-prometheus -n monitoring 4001:9090
