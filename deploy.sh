#!/bin/bash

#docker rmi -f $(docker images -a -q)

#fetch GKE credentails for Kubectl
gcloud container clusters get-credentials standard-cluster-1 --zone us-central1-a --project sample-project

DOCKERIMAGE=`env | grep -i "BUILD_DISPLAY_NAME" | awk '{print $2}'`

template=`cat kube-scripts/flask-app.yaml | sed "s#{{DOCKER_IMAGE}}#$DOCKERIMAGE#"`

# apply the yml with the substituted value

echo "$template" | kubectl apply -f -

echo "$DOCKERIMAGE"

kubectl apply -f kube-scripts/flask-svc.yaml
#See the rolling update in action
kubectl rollout status deployment api-deployment 
