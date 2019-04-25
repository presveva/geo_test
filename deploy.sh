#!/bin/bash
docker build --rm -f "Dockerfile" -t unrealists:latest .
docker tag unrealists gcr.io/cdn-dinoia/unrealists:latest

docker push gcr.io/cdn-dinoia/unrealists:latest
gcloud compute instances update-container unrealists --zone europe-west3-c --project cdn-dinoia

aplay /usr/share/sounds/purple/alert.wav
