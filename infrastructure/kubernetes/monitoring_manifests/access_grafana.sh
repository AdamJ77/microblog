#!/bin/bash

# Expose Grafana service (localhost:4000 - default authentication - admin/prom-operator)
kubectl port-forward svc/prometheus-grafana -n monitoring 4000:80
