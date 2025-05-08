# Weather App

A comprehensive weather application that retrieves current weather data from [OpenWeather](https://openweathermap.org/current) API. This project demonstrates a complete cloud-native application stack including a Python Flask web server, containerization with Docker, Kubernetes deployment using Helm charts, and infrastructure provisioning with Terraform.

## Project Overview

This application provides real-time weather information for London (configurable to other locations) through a simple web interface. It's designed as a microservice with health checks and monitoring endpoints, containerized for consistent deployment across environments, and includes infrastructure-as-code for cloud deployment.

## Repository Structure

The repository contains three independent components, each with its separate README.md file:

- [Application](app/README.md) - Python Flask web server that retrieves and displays weather data
- [Helm Chart](helm/README.md) - Kubernetes deployment configuration for the weather application
- Terraform Infrastructure - AWS infrastructure provisioning code for production deployment

## Features

- Current weather information display
- Health check endpoint
- Containerized application
- Kubernetes deployment configuration
- Horizontal Pod Autoscaling
- Infrastructure-as-code for AWS deployment

## Technology Stack

- **Backend**: Python 3.11, Flask 3.0
- **API Integration**: OpenWeather API
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Package Management**: Helm
- **Infrastructure**: Terraform, AWS (EKS, ECR, VPC)

## Prerequisites

- Docker
- Kubernetes cluster (Minikube for local development)
- Helm
- Skaffold (for local development)
- OpenWeather API key
- AWS account (for production deployment)
- Terraform (for infrastructure provisioning)

## Quick Start

### Local Development with Docker

1. Clone the repository:
   ```
   git clone <repository-url>
   cd weather-app
   ```

2. Set up environment variables:
   ```
   cd app
   cp .env.example .env
   ```
   Edit `.env` and add your OpenWeather API key.

3. Build and run with Docker:
   ```
   docker build -t localhost:weather .
   docker run --rm -p 8080:8080 -d --name web localhost:weather
   ```

4. Access the application at http://localhost:8080

### Local Kubernetes Deployment

1. Start Minikube:
   ```
   minikube start --profile custom
   ```

2. Configure Skaffold:
   ```
   source <(minikube docker-env -p custom)
   skaffold config set --kube-context custom local-cluster true
   skaffold dev
   ```

3. In a separate terminal, enable external access:
   ```
   minikube tunnel -p custom
   ```

4. Access the application using the external IP:
   ```
   kubectl get svc -n app
   ```
   Open your browser at `http://<EXTERNAL-IP>:8080`

## Production Deployment

### AWS Deployment

1. Configure AWS credentials
2. Initialize Terraform:
   ```
   cd terraform
   terraform init
   terraform plan
   terraform apply
   ```

3. Configure kubectl to use the new EKS cluster
4. Deploy the application:
   ```
   helm upgrade --install weather ./helm/weather -n app --create-namespace
   ```

## API Endpoints

- `/` - Current weather information in HTML format
- `/ping` - Simple ping endpoint (returns "Pong")
- `/health` - Health check endpoint (returns JSON status)

## Configuration

The application can be configured using environment variables:

- `API_URL` - OpenWeather API URL
- `API_KEY` - Your OpenWeather API key
- `LATITUDE` - Latitude for weather location (default: London)
- `LONGITUDE` - Longitude for weather location (default: London)

