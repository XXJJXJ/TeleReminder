# Developer Guide [Incomplete...]

```bash
python3 -m venv .venv # creates virtual environment

source .venv/bin/activate # activate virtual environment, to install any dependencies that macos disallow

pip install -r requirements.txt # install project dependencies

source deactivate # deactivate venv
```

# Deployment Guide

* Couldn't get the zip files method to work (dependencies not found)

* Attempted the container image method with docker etc. Steps taken are as follows
[Guide](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html)

## 1. Install aws cli v2
[Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

## 2. Build project based on AWS Base Images (Python) 
[Guide](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html#python-image-instructions)
    - Notable commands: `docker build --platform linux/amd64 -t <image_name>:<tag> .`
    - Just follow the steps in this section... until image is built

## 3a. AWS Configure
Create a IAM User in AWS and grant it AdministratorAccess (Attach a Policy to it) [Pretty sure this is an overkill but works for now]

## 3b. Deploying Images on AWS:

On our local commandline execute

```bash
aws ecr get-login-password --region <Region> | docker login --username AWS --password-stdin <AWS_ACC_ID>.dkr.ecr.<Region>.amazonaws.com
```

E.g. 
```bash
aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin <AWS_ACC_ID>.dkr.ecr.ap-southeast-1.amazonaws.com
```

## 4. Create repository

aws ecr create-repository --repository-name tms-reminder-bot --region ap-southeast-1 --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE

## 5. Copy the repositoryUri from the output in the previous step then docker tag

```bash
docker tag docker-image:test <repositoryUri>:latest
```

## 6. Docker push
```bash
docker push <repositoryUri>:latest
```

## 7. Create Lambda on the AWS console platform using the container image option
- UI self explanatory
- NOTE: If built for Linux/Windows please choose x86_64 architecture...


## 8. Setup cloud watch, eventbridge scheduler
...



# Update procedure

## 1. Modify and change code as you like
## 2. Build the image: `docker build --platform linux/amd64 -t reminder-bot:<new_tag> .`
## 3. Retag newest image as aws image: `docker tag reminder-bot:<new_tag> <AWS_ACC_ID>.dkr.ecr.ap-southeast-1.amazonaws.com/tms-reminder-bot:latest`
## 4a. AWS configure with IAM account (only if not logged in)
* Either:
    - If authorization token has expired and needs to reauthenticate: `aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin <AWS_ACC_ID>.dkr.ecr.ap-southeast-1.amazonaws.com`
    - For first timer: `aws configure`

## 4b. Push to image to AWS: `docker push <AWS_ACC_ID>.dkr.ecr.ap-southeast-1.amazonaws.com/<image_name>:latest`
## 5. Update function image in AWS Console