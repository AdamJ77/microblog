#!/bin/bash

CREDENTIALS=$(az ad sp create-for-rbac --role="Monitoring Reader" --scopes="/subscriptions/XYZ/resourceGroups/Microblog1")

echo "Use these credentials to add Azure Monitor Data Source in Grafana"
echo $CREDENTIALS
echo "Then import dashboard ID 10956"
