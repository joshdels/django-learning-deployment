# django-learning-deployment
this is a practice django practices for deployment
how do you learn 
    1. from shortcuts (memorize)
    2. from official docs
    3. from source code 

__
### installation of docker
1. install unbuntu
2. configure wsl2 virtually using bios
3. open docker desktop

### Use of Docker
Dockerfile 
docker-compose.yml
.dockerignore 

### cmd commands for docker
docker build .
docker-compose up
docker-compose up -d -->(detach)
docker-compose exec [service for python cmds]
docker-compose down --> stop server
docker-compose 

### Security
docker-compose exec web python -c "import secrets; print(secrets.token_urlsafe(38))" --> for production yml
docker-compose exec web python manage.py check --deploy


### removing images clearly
docker-compose down --rmi all --> removes all 
docker system prune -f --> deletes images
docker-compose build --no-cache

---
## Notes
1. AbstractUser (Little since added already)vs. AbstractBaseUser (Full Manual)
2. Collectstatic for production ready => STATIC_ROOT, STATICFILES_DIR, STATIC_STORAGE
3. allauths
4. Deployment
5. Local Development (file: docker-compose.yml) / Productio (file: docker-compose-prod.yml)n --> all controlled in the docker 

### deploying for vultr
ssh root@IP address
password
--
#### installing Docker
sudo apt update && sudo apt upgrade -y
sudo apt install -y docker.io
sudo apt install -y docker-compose
sudo systemctl enable docker
sudo systemctl start docker
docker --version
docker-compose --version