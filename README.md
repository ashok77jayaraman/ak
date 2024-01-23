# Project Documentation: Flask Application Deployment with Jenkins CI/CD

## Overview

This document provides detailed information on the setup and deployment process of a Flask web application using Jenkins for Continuous Integration and Continuous Deployment (CI/CD). The application is containerized with Docker and deployed to a Kubernetes cluster.

### Project Components

1. **Flask Application:**
   - Framework: Flask 2.0.1
   - Dependencies: Werkzeug 2.0.1
   - Deployment: Docker, Kubernetes

2. **CI/CD Tools:**
   - Jenkins

## Jenkins Pipeline

### Pipeline Structure

The Jenkins pipeline is structured into stages, each responsible for specific tasks in the CI/CD process.

1. **Git:**
   - Clone the source code from the GitHub repository.

2. **Docker:**
   - Build a Docker image from the source code.
   - Log in to DockerHub using credentials stored in Jenkins.
   - Push the Docker image to DockerHub.

3. **Kubernetes:**
   - Delete the existing Kubernetes deployment and service.
   - Create a new Kubernetes deployment and service using configuration files.

### Jenkinsfile

```groovy
pipeline {
    agent none
    environment {
        DOCKERHUB_CREDENTIALS = credentials("347f96c5-a65c-4802-a84a-7b3b4d21572b")
    }
    stages {
        stage('Git') {
            agent {
                label 'k8s-master'
            }
            steps {
                script{
                    git 'https://github.com/ashok77jayaraman/ak.git'
                }
            }
        }
        stage('Docker') {
            agent {
                label 'k8s-master'
            }
            steps {
                sh 'sudo docker build /home/ubuntu/jenkins/workspace/pr2/ -t ashok77jayaraman/h3'
                sh 'sudo docker login -u ${DOCKERHUB_CREDENTIALS_USR} -p ${DOCKERHUB_CREDENTIALS_PSW} '
                sh 'sudo docker push ashok77jayaraman/h3'
            }
        }
        stage('k8s') {
            agent {
                label 'k8s-master'
            }
            steps {
                sh 'kubectl delete deployment flask-login-app'
                sh 'kubectl delete svc my-own'
                sh 'kubectl create -f /home/ubuntu/jenkins/workspace/pr2/deploy.yaml'
                sh 'kubectl create -f /home/ubuntu/jenkins/workspace/pr2/service.yaml'
            }
        }
    }
}
```

## Setup Instructions

### Prerequisites

1. **Jenkins Server:**
   - Install Jenkins on a dedicated server.
   - Configure Jenkins with necessary plugins, including Git, Docker, and Kubernetes.

2. **Jenkins Credentials:**
   - Create a Jenkins credential with ID "347f96c5-a65c-4802-a84a-7b3b4d21572b" for DockerHub authentication.

3. **Kubernetes Cluster:**
   - Set up a Kubernetes cluster with a master node and worker nodes.

### Jenkins Configuration

1. **Install Required Jenkins Plugins:**
   - Install plugins for Git, Docker, Kubernetes, and any other necessary plugins.

2. **Configure Jenkins Global Credentials:**
   - Add DockerHub credentials with ID "347f96c5-a65c-4802-a84a-7b3b4d21572b."

### Application Source Code

1. **GitHub Repository:**
   - Maintain the Flask application source code in a GitHub repository.

### Deployment Configuration

1. **Dockerfile:**
   - Create a Dockerfile specifying the application dependencies and build process.

2. **Kubernetes Configuration:**
   - Prepare Kubernetes deployment and service YAML files (`deploy.yaml` and `service.yaml`).

## Usage

1. **Run Jenkins Pipeline:**
   - Trigger the Jenkins pipeline manually or set up automatic triggers (e.g., webhook integration).

2. **Monitor Jenkins Build:**
   - Monitor Jenkins build logs and console output for any errors or issues.

3. **Access Deployed Application:**
   - Access the deployed Flask application using the external IP and NodePort specified in the Kubernetes service.

## Troubleshooting

If you encounter any issues during the CI/CD process, refer to the Jenkins build logs, Docker logs, and Kubernetes logs for detailed information on errors. Inspect the Jenkinsfile for any misconfigurations or missing steps.

## Conclusion

This document provides a comprehensive guide to deploying a Flask application using Jenkins CI/CD with Docker and Kubernetes. Follow the setup instructions carefully, and refer to the troubleshooting section if needed. Continuous monitoring and improvement of the CI/CD pipeline will ensure a streamlined development and deployment process.
