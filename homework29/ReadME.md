# Homework_29 - Flask App

This is a simple Flask application that randomly displays GIFs of cats.

## Requirements

- Docker

Install Docker following instructions [here](https://docs.docker.com/get-docker/).

## Running the Application with Docker
To build and run the application using Docker, follow these instructions:

1. Build the Docker Image
Navigate to your project directory and create the Docker image with the following command

```bash
docker build -t flask-app .
```

2. Launch the Docker Container
Start the Docker container with the appropriate port mapping:

```bash
docker run -p 8866:5000 flask-app
You can access the application at http://localhost:8866.
```

Project Structure
```
├── app.py               # The main file containing the Flask application
├── requirements.txt     # File listing the Python dependencies
├── Dockerfile           # Docker configuration file for image creation
└── templates
    └── index.html       # HTML template for displaying the cat GIFs
```

### Stopping and Removing the Container
```
docker stop my-python-app
docker rm my-python-app
```