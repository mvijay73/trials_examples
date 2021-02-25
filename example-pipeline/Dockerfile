# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:2

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY src/. /app
COPY .bashrc /root

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD /bin/bash

