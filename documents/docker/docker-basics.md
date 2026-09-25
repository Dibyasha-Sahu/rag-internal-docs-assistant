# Docker Basics

## What is Docker?

Docker is a containerization platform that packages an application and its dependencies into a container.

Containers provide a consistent environment so applications can run reliably across development, testing, and production environments.

## Docker Image

A Docker image is a read-only template used to create containers.

An image contains:

- Application code
- Runtime environment
- Dependencies
- Configuration
- Required system libraries

Images are commonly built using a Dockerfile.

## Docker Container

A Docker container is a running instance of a Docker image.

Containers are isolated from each other while sharing the host operating system kernel.

## Dockerfile

A Dockerfile is a text file containing instructions used to build a Docker image.

Common Dockerfile instructions include:

- FROM
- WORKDIR
- COPY
- RUN
- ENV
- EXPOSE
- CMD
- ENTRYPOINT

Example Dockerfile:

    FROM python:3.11-slim

    WORKDIR /app

    COPY requirements.txt .

    RUN pip install --no-cache-dir -r requirements.txt

    COPY . .

    EXPOSE 8000

    CMD ["python", "app.py"]

## Docker Build

The docker build command creates a Docker image from a Dockerfile.

Example:

    docker build -t my-app:1.0 .

Here:

- -t assigns a name and tag to the image.
- . specifies the build context.

## Docker Run

The docker run command creates and starts a container from an image.

Example:

    docker run -d -p 8000:8000 my-app:1.0

The -d option runs the container in detached mode.

The -p option maps a host port to a container port.

## Docker Port Mapping

Port mapping allows applications running inside containers to be accessed from the host system.

Example:

    docker run -d -p 8080:80 nginx

This maps:

- Host port: 8080
- Container port: 80

The application can then be accessed through port 8080 on the host.

## Docker Volumes

Docker volumes provide persistent storage for containers.

Without persistent storage, data created inside a container may be lost when the container is removed.

Example:

    docker volume create app-data

## Docker Network

Docker networks allow containers to communicate with each other.

Containers connected to the same Docker network can communicate using container or service names.

Example:

    docker network create app-network

## Docker Registry

A Docker registry stores and distributes Docker images.

Examples include:

- Docker Hub
- GitHub Container Registry
- Amazon Elastic Container Registry

## Docker Compose

Docker Compose is used to define and run multi-container applications using a YAML configuration file.

A Compose configuration can define:

- Application services
- Networks
- Volumes
- Environment variables
- Port mappings

## Why Docker Matters

Docker makes application packaging and deployment more consistent by providing portable, isolated, and reproducible environments.

Docker is commonly used in DevOps workflows for application packaging, CI/CD pipelines, testing, and Kubernetes deployments.