# GitHub Actions Basics

## What is GitHub Actions?

GitHub Actions is a CI/CD automation platform integrated with GitHub.

It allows workflows to automatically run tasks when events occur in a repository, such as pushing code, creating a pull request, or creating a release.

## GitHub Actions Workflow

A workflow is an automated process defined in a YAML file.

Workflow files are stored in:

    .github/workflows/

A workflow can contain one or more jobs.

## Workflow File

A GitHub Actions workflow is written using YAML.

A basic workflow can look like:

    name: CI

    on:
      push:
      pull_request:

    jobs:
      test:
        runs-on: ubuntu-latest

        steps:
          - name: Checkout repository
            uses: actions/checkout@v4

          - name: Run tests
            run: echo "Running tests"

## Workflow Trigger

A trigger determines when a GitHub Actions workflow starts.

Common triggers include:

- push
- pull_request
- workflow_dispatch
- schedule

For example:

    on:
      push:
        branches:
          - main

This workflow runs when code is pushed to the main branch.

## Jobs

A job is a group of steps that runs on a runner.

A workflow can contain multiple jobs.

Example:

    jobs:
      test:
        runs-on: ubuntu-latest

        steps:
          - name: Checkout code
            uses: actions/checkout@v4

          - name: Run tests
            run: pytest

## Steps

Steps are individual tasks inside a job.

A step can:

- Run a shell command
- Execute a script
- Use an existing GitHub Action
- Install dependencies
- Run tests
- Build an application
- Perform security checks

## GitHub Actions Runner

A runner is the machine that executes a GitHub Actions job.

GitHub-hosted runners provide environments such as:

- Ubuntu
- Windows
- macOS

For example:

    runs-on: ubuntu-latest

## Actions

Actions are reusable components that perform specific tasks.

For example:

    uses: actions/checkout@v4

The checkout action downloads the repository code into the runner so that later steps can work with it.

## CI Pipeline

A Continuous Integration pipeline commonly performs:

1. Checkout source code
2. Install dependencies
3. Run linting
4. Run unit tests
5. Run security checks
6. Build the application

The purpose is to detect problems early and validate changes automatically.

## CD Pipeline

A Continuous Delivery or Continuous Deployment pipeline can automatically:

- Build application artifacts
- Build Docker images
- Push images to a container registry
- Deploy applications
- Verify deployments

## Environment Variables and Secrets

GitHub Actions supports environment variables for configuration.

Sensitive information such as API keys, passwords, and tokens should be stored as GitHub Actions secrets rather than directly inside workflow files.

Example:

    env:
      APP_ENV: production

Secrets can be referenced using:

    ${{ secrets.API_KEY }}

Secrets should never be committed directly to a repository.

## GitHub Container Registry

GitHub Container Registry, also known as GHCR, can store Docker container images.

A CI/CD workflow can:

1. Build a Docker image
2. Authenticate with GHCR
3. Push the image to GHCR
4. Use the image for deployment

## Security in GitHub Actions

Security checks can be included in CI/CD workflows.

Common security tools include:

- Gitleaks for detecting exposed secrets
- Trivy for container and dependency vulnerability scanning
- Checkov for Infrastructure as Code security scanning

Security validation helps identify issues before applications are deployed.

## GitHub Actions and Docker

GitHub Actions can automate Docker image builds.

Example:

    docker build -t my-app:1.0 .

A workflow can then push the image to a container registry.

## GitHub Actions and Kubernetes

GitHub Actions can also automate Kubernetes deployments.

A typical deployment workflow can include:

1. Run tests
2. Run security checks
3. Build Docker image
4. Push image to registry
5. Deploy to Kubernetes
6. Verify deployment

## Why GitHub Actions Matters

GitHub Actions helps automate software delivery by connecting source control, testing, security validation, Docker image building, container registries, and deployment processes into a repeatable CI/CD workflow.