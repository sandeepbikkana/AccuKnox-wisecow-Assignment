# wisecow-Assignment...
■ Wisecow Zero-Trust Deployment on Amazon
EKS (with CI/CD)
This project demonstrates a fully automated CI/CD pipeline for deploying the Wisecow application
on Amazon EKS using GitHub Actions. It integrates NGINX Ingress Controller and KubeArmor
Zero-Trust Security Policies for runtime protection.

Components Used:
1 Amazon EKS - Managed Kubernetes cluster
2 Amazon ECR - Private Docker image registry
3 GitHub Actions - CI/CD automation
4 NGINX Ingress Controller - For external traffic routing
5 KubeArmor - Runtime security (Zero Trust policies)
6 Wisecow App - Sample  application

Prerequisites:
1 AWS account with permissions for EKS, ECR, EC2, IAM, and VPC
2 `aws-cli`, `kubectl`, and `eksctl` installed
3 GitHub repository with secrets configured: AWS_ACCESS_KEY_ID,
AWS_SECRET_ACCESS_KEY, AWS_REGION, ECR_REPOSITORY,
EKS_CLUSTER_NAME

Step 1: Create EKS Cluster
Command: eksctl create cluster --name wisecow-cluster --region ap-south-1 --nodegroup-name
wisecow-nodes --node-type t3.medium --nodes 2 --managed
Verify with: kubectl get nodes

Step 2: Create ECR Repository
aws ecr create-repository --repository-name wisecow --region ap-south-1

Step 3: Configure GitHub Secrets
Add the following secrets in GitHub Actions settings: AWS_ACCESS_KEY_ID,
AWS_SECRET_ACCESS_KEY, AWS_REGION, ECR_REPOSITORY, EKS_CLUSTER_NAME

Step 4: GitHub Actions CI/CD Workflow
The pipeline builds and pushes a Docker image to ECR, installs the NGINX ingress controller, and
deploys the Wisecow application to EKS.

Step 6: Deploy KubeArmor (Zero-Trust)
Install Helm chart: helm repo add kubearmor https://kubearmor.github.io/charts && helm install
kubearmor kubearmor/kubearmor -n kubearmor --create-namespace
Apply policy file: kubectl apply -f k8s/kubearmor-wisecow-policy.yaml

Step 7: Validate Policy
Run: kubectl exec -it -- sh -c 'echo hacked > /etc/testfile' — should show 'Permission denied'.
Logs: kubectl logs -n kubearmor -l kubearmor-app=kubearmor --tail=100 | grep -i 'policy'

Troubleshooting:
1 Policy cannot be enforced: Ensure app label matches in KubeArmor policy.
2 Ingress not resolving: Check LoadBalancer external IP with 'kubectl get ingress'.
3 403 Forbidden: Ensure target port and ingress host are configured properly.
