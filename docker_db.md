<!--  -->
docker run -ti -d -p 27017:27017 mongo:latest -v ./team6Container/mongodb_data:/data/db

<!-- to run application -->
docker compose up -d