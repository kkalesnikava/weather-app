# Helm chart for sample Python weather webserver 

Helm chat for sample Python weather webserver. Details about the app and how to deploy the app to minikube cluster using helm chart and skaffold can be found [here](../app/README.md).

## Structure 
- `weather` - helm chart contains basic templates to create deployment, service, ingress and hpa
- `weather/values.yaml` - file to setup and configure default chart variables
