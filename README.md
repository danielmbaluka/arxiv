# Arxiv newsfeed
A simple webapp that scrapes [arxiv.org](https://arxiv.org/) for the latest articles in psychiatry, therapy, data science and machine learning.

The application is made up of a REST API written in [Django](https://docs.djangoproject.com/en/3.2/) and a simple web ui written in [Angular](https://angular.io/)

## Running the application
### Prerequisite
- [git](https://git-scm.com/)
- [docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/install/)

Clone the application through git

    git clone https://github.com/danielmbaluka/arxiv.git

Start both the API and the web UI using docker-compose
    
    docker-compose up

Note: 
1. This will take several minutes (to download the docker images) and build images for the application. Depending on your network speed, it might take more than 10 minutes
2. Scraping of the articles happens in the background (via celery tasks). The tasks that scraps the articles runs at 10 minutes intervals, so it might take ~10 minutes before any articles appear on the web ui

### Accessing the application
The web UI runs can be accessed on `http://localhost:4200` while the API can be accessed on `http://localhost:8001/api/v1`
