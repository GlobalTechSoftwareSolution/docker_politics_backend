#!/bin/bash

# Script to build, tag, and push the politics_backend Docker image to existing Docker Hub repo

echo "Building the Docker image..."
docker build -t politics_backend .

if [ $? -ne 0 ]; then
    echo "Error: Failed to build Docker image"
    exit 1
fi

# Tag with the existing repository name
echo "Tagging the image as manibharadwajcr/politics-backend:latest..."
docker tag politics_backend manibharadwajcr/politics-backend:latest

if [ $? -ne 0 ]; then
    echo "Error: Failed to tag Docker image"
    exit 1
fi

# Also tag with a new specific tag
NEW_TAG="8003-deploy-$(date +%Y%m%d-%H%M%S)"
echo "Tagging the image as manibharadwajcr/politics-backend:${NEW_TAG}..."
docker tag politics_backend manibharadwajcr/politics-backend:${NEW_TAG}

if [ $? -ne 0 ]; then
    echo "Error: Failed to tag Docker image with new tag"
    exit 1
fi

echo "Pushing the image to Docker Hub (latest)..."
docker push manibharadwajcr/politics-backend:latest

if [ $? -ne 0 ]; then
    echo "Error: Failed to push Docker image (latest) to Docker Hub"
    exit 1
fi

echo "Pushing the image to Docker Hub (${NEW_TAG})..."
docker push manibharadwajcr/politics-backend:${NEW_TAG}

if [ $? -ne 0 ]; then
    echo "Error: Failed to push Docker image (${NEW_TAG}) to Docker Hub"
    exit 1
fi

echo "✅ Successfully built and pushed images to Docker Hub!"
echo ""
echo "Images pushed:"
echo "- manibharadwajcr/politics-backend:latest"
echo "- manibharadwajcr/politics-backend:${NEW_TAG}"
echo ""
echo "To run the image locally, use:"
echo "docker run -p 8003:8003 manibharadwajcr/politics-backend:latest"
echo ""
echo "The application is configured to run on port 8003 with:"
echo "- Registration: POST /api/register/"
echo "- Login: POST /api/login/"
echo "- All other API endpoints working as expected"