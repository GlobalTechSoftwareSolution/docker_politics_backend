#!/bin/bash

# Script to build and push cross-platform Docker image for politics_backend

echo "Building cross-platform Docker image for linux/amd64..."
docker buildx build --platform linux/amd64 -t politics_backend .

if [ $? -ne 0 ]; then
    echo "Error: Failed to build Docker image for linux/amd64"
    exit 1
fi

# Tag with the existing repository name
echo "Tagging the image as manibharadwajcr/politics-backend:linux-amd64..."
docker tag politics_backend manibharadwajcr/politics-backend:linux-amd64

if [ $? -ne 0 ]; then
    echo "Error: Failed to tag Docker image"
    exit 1
fi

# Also tag as latest
echo "Tagging the image as manibharadwajcr/politics-backend:latest..."
docker tag politics_backend manibharadwajcr/politics-backend:latest

if [ $? -ne 0 ]; then
    echo "Error: Failed to tag Docker image"
    exit 1
fi

echo "Pushing the linux/amd64 image to Docker Hub..."
docker push manibharadwajcr/politics-backend:linux-amd64

if [ $? -ne 0 ]; then
    echo "Error: Failed to push Docker image to Docker Hub"
    exit 1
fi

echo "Pushing the latest image to Docker Hub..."
docker push manibharadwajcr/politics-backend:latest

if [ $? -ne 0 ]; then
    echo "Error: Failed to push Docker image to Docker Hub"
    exit 1
fi

echo "✅ Successfully built and pushed linux/amd64 compatible images to Docker Hub!"
echo ""
echo "To run on your Linux server, use:"
echo "docker run -p 8003:8003 manibharadwajcr/politics-backend:linux-amd64"
echo ""
echo "Or simply:"
echo "docker run -p 8003:8003 manibharadwajcr/politics-backend:latest"
echo ""
echo "The application will be accessible at http://your-server-ip:8003"