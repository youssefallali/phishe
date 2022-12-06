# Dockerfile

# Author       : youssef
# Github       : https://github.com/youssef
# Email        : youssefallali210@gmail.com
# Date         : 08-08-2022
# Main Language: Python

# Download and import main images

# Operating system
FROM debian:latest
# Main package
FROM python:3

# Author info
LABEL MAINTAINER="https://github.com/youssefallali/phishe"

# Working directory
WORKDIR MaxPhisher/
# Add files 
ADD . /MaxPhisher

# Installing other packages
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install php openssh-client -y
RUN pip3 install -r files/requirements.txt
RUN apt-get clean

# Main command
CMD ["python3", "phishe.py", "--noupdate"]

## Wanna run it own? Try following commnads:

## "sudo docker build . -t youssefallali/phishe:latest", "sudo docker run --rm -it youssefallali/phishe:latest"

## "sudo docker pull youssefallali/phishe", "sudo docker run --rm -ityoussefallali/phishe"
