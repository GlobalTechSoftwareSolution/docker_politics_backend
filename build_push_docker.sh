#!/bin/bash

# Script to build, tag, and push the politics_backend Docker image to Docker Hub

echo "Enter your Docker Hub username:"
read DOCKER_USERNAME

if [ -z "$DOCKER_USERNAME" ]; then
    echo "Error: Docker Hub username is required"
    exit 1
fi

IMAGE_NAME="politics_backend"
TAGGED_IMAGE="${DOCKER_USERNAME}/${IMAGE_NAME}:latest"

echo "Building the Docker image..."
docker build -t $IMAGE_NAME .

if [ $? -ne 0 ]; then
    echo "Error: Failed to build Docker image"
    exit 1
fi

echo "Tagging the image as ${TAGGED_IMAGE}..."
docker tag $IMAGE_NAME $TAGGED_IMAGE

if [ $? -ne 0 ]; then
    echo "Error: Failed to tag Docker image"
    exit 1
fi

echo "Pushing the image to Docker Hub..."
docker push $TAGGED_IMAGE

if [ $? -ne 0 ]; then
    echo "Error: Failed to push Docker image to Docker Hub"
    exit 1
fi

echo "Successfully built and pushed ${TAGGED_IMAGE} to Docker Hub!"
echo ""
echo "To run the image locally, use:"
echo "docker run -p 8003:8003 $TAGGED_IMAGE"
echo ""
echo "To run with docker-compose, update your docker-compose file to use the image:"
echo "services:"
echo "  backend:"
echo "    image: $TAGGED_IMAGE"
echo "    ports:"
echo "      - \"8003:8003\""