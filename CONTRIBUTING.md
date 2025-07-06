# CONTRIBUTING

# HOW TO RUN DOCKERFILE LOCALLY

docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE_NAME sh -c "flask run --host"