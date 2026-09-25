# Kubernetes Basics

## What is Kubernetes?

Kubernetes is a container orchestration platform used to deploy, manage, scale, and maintain containerized applications.

It automates many tasks involved in running containers across a cluster.

## Kubernetes Cluster

A Kubernetes cluster is a group of machines that work together to run containerized applications.

A cluster generally contains:

- Control plane
- Worker nodes

The control plane manages the cluster, while worker nodes run application workloads.

## Kubernetes Pod

A Pod is the smallest deployable unit in Kubernetes.

A Pod can contain one or more containers that share networking and storage resources.

Example:

    kubectl get pods

This command lists the Pods in the current namespace.

## Kubernetes Deployment

A Deployment manages the desired number of replicas of an application.

It can:

- Create Pods
- Maintain the desired number of replicas
- Perform rolling updates
- Replace failed Pods

Example:

    kubectl create deployment nginx --image=nginx

## Kubernetes Service

A Service provides a stable network endpoint for accessing Pods.

Services are useful because Pod IP addresses can change when Pods are recreated.

Common Service types include:

- ClusterIP
- NodePort
- LoadBalancer

Example:

    kubectl expose deployment nginx --port=80

## Kubernetes Namespace

A Namespace provides logical isolation for resources inside a Kubernetes cluster.

Namespaces can be used to organize applications and separate environments.

Example:

    kubectl create namespace devops

## ConfigMap

A ConfigMap stores non-sensitive configuration data.

Configuration values can be provided to containers through environment variables or mounted files.

## Secret

A Secret is used to store sensitive configuration data such as:

- Passwords
- API keys
- Tokens
- Credentials

Secrets should be handled carefully and should not be committed directly to source control.

## Kubernetes Configurations

Kubernetes resources are commonly defined using YAML manifests.

A YAML manifest can describe resources such as:

- Deployment
- Service
- ConfigMap
- Secret
- Namespace
- ServiceAccount

Example:

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: nginx
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
            - name: nginx
              image: nginx

## kubectl

kubectl is the command-line tool used to communicate with a Kubernetes cluster.

Common commands include:

    kubectl get pods

    kubectl get deployments

    kubectl get services

    kubectl describe pod <pod-name>

    kubectl logs <pod-name>

    kubectl apply -f deployment.yaml

    kubectl delete -f deployment.yaml

## Kubernetes Scaling

Kubernetes can scale applications by changing the number of Pod replicas.

Example:

    kubectl scale deployment nginx --replicas=3

This changes the desired number of replicas to three.

## Kubernetes Rolling Updates

Kubernetes Deployments support rolling updates.

A rolling update gradually replaces old Pods with new Pods so that application availability can be maintained during an update.

## Kubernetes Health Checks

Kubernetes supports health checks for containers.

Common probes include:

- Liveness probe
- Readiness probe
- Startup probe

A liveness probe helps determine whether a container should be restarted.

A readiness probe determines whether a container is ready to receive traffic.

A startup probe can be used when an application needs additional time to start.

## Kubernetes Resource Requests and Limits

Resource requests specify the amount of CPU and memory a container is expected to need.

Resource limits specify the maximum CPU and memory a container can use.

Example:

    resources:
      requests:
        cpu: "100m"
        memory: "128Mi"
      limits:
        cpu: "500m"
        memory: "512Mi"

## Kubernetes Service Account and RBAC

A ServiceAccount provides an identity for workloads running inside Kubernetes.

Role-Based Access Control, or RBAC, controls what users and workloads are allowed to do.

Common RBAC resources include:

- Role
- ClusterRole
- RoleBinding
- ClusterRoleBinding

RBAC follows the principle of giving workloads only the permissions they require.

## Kubernetes and Docker

Docker can be used to build container images that are then deployed to Kubernetes.

A common workflow is:

1. Build a Docker image
2. Store the image in a container registry
3. Deploy the image using Kubernetes
4. Expose the application using a Service
5. Monitor the application

## Kubernetes and DevOps

Kubernetes is commonly used in DevOps workflows for:

- Container orchestration
- Application deployment
- Scaling
- Rolling updates
- Service discovery
- Health monitoring
- Resource management

## Why Kubernetes Matters

Kubernetes provides a consistent platform for deploying and managing containerized applications.

It helps automate application deployment, scaling, networking, updates, and recovery across a cluster.