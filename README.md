# DevOps home assignment

This repository contains a home assignment code for DevOps Engineer.


## Task

0. Fork this repo - use https or ssh we do'nt care :).
1. Create a deployable docker image for the application and publish it to docker-hub.
    - Feel free to use docker multi-stage layer.
    - Feel free to add .dockerignore file before publish the docker image :)
    - Feel free to switch up technologies.  For Example: chose other docker runtime ( CRI-O and etc..)
2. Create a Kubernetes deployment and service for the application.
    - Just aim for the simplest setup, no ingress deployment is needed.
    - Feel free to use Helm.
    - You can use [kind](https://kind.sigs.k8s.io/), [Minikube](https://minikube.sigs.k8s.io/docs/start/), [k3s](https://k3s.io/), [k0s](https://k0sproject.io/), [microk8s](https://microk8s.io/), [okd](https://www.okd.io/) or any other Kubernetes distribution you are familiar with.
3. Create automation to build, test and deploy the application when a change happens in git.
    - Feel free to switch up technologies. For example you can use an Ansible playbook, github actions, Azure Pipelines, gitlab CI or Jenkins  pipeline.
4. Bonus: Use ArgoCD or Argo-Core
5. Send us  link to the fork where you did your work + link to docker-hub (or other docker registry).

### Notes

- DevOps rocks!!!
- Explain as much as possible in the commit message(s) and/or comments if needed. 
- It would be great if you'd also write about why you choose a certain technology if there are alternatives to consider.
- Good Luck!
