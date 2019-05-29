FROM python:3.7.3-stretch
LABEL MAINTAINER="Aleksa Sukovic"

COPY ./src /usr/src/app
COPY ./.devcontainer/settings.vscode.json /root/.vscode-remote/data/Machine/settings.json

RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt