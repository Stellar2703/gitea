# Gitea with MySQL - Docker Compose Setup

This repository provides a simple setup for running [Gitea](https://gitea.io/en-us/) (a self-hosted Git service) with a MySQL database using Docker Compose.

## Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

Use the yqml file and use docker compose up -d


New Changes Made in the app.ini

1. Limited the users to create zero repositories
2. no user except admin user can create and run organizations in the service
3. Limited max_size of a file to be uploaded in a repository to 30 mib
