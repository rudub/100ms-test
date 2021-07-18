# 100ms-test

This is simple Python application to print URL and  parameters/args on HTTP request

The application is using python flask.

To deploy application git clone to the repository git clone https://github.com/rudub/100ms-test

Build the docker image via docker build -t docker-handle/imagename:tag Dockerfile

Ready image available on github with user ruchi183/100ms:v2

To deploy the image k8s helm-chart is deployed.

All the above steps is automated via github actions on push to main branch event.

Workflow is avilable in .github/workflows/main.yaml

The application is exposed on nginx ingress and ingress route is mentioned in ingress.yaml

Nginx controller is deployed on EKS via helm chart

