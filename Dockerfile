# Download base image ubuntu 22.04
FROM ubuntu:22.04

# LABEL about the custom image
LABEL maintainer="gotchab@gmail.com"
LABEL version="1.0"
LABEL description="This is custom Docker Image for \
presenting current weather in Tel Aviv."

# Disable Prompt During Packages Installation
#ARG DEBIAN_FRONTEND=noninteractive

# Update Ubuntu Software repository
RUN apt update

RUN apt-get install -y locales locales-all
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

RUN apt-get install ca-certificates -y
RUN update-ca-certificates

# Copy weather binary 
COPY weather /usr/bin/weather  
RUN /bin/bash
