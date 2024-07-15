# Python weather webserver app and infrastructure setup

The repository contains 3 independent components, each with its separate README.md file:
- [Application](app/README.md) - code for weather webserver app written in Python and documentation on how the application is organized and how to run it
- [Helm chart](helm/README.md) - helm chart for weather webserver Python app
- Terraform infrastructure - terraform infrastructure code to create VPC, subnets, routing tables, NAT gateways, EKS cluster and ECR on AWS required for weather webserver app setup.
