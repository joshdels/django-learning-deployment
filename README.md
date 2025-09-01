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
sudo systemctl enable docker --> running 24/7
sudo systemctl start docker
docker --version
docker-compose --version

#### Running a VPS
- for running using git uploads
apt update && apt install -y git --> git for cloning
git clone https://github.com/USERNAME/REPO_NAME.git /root/myapp
cd /root/myapp
docker-compose up -d
- for running locally pc
scp -r ./myapp root@YOUR_SERVER_IP:/root/myapp

#### adding production keys to VULTR
cd /root/myapp
nano docker-compose.prod.yml --> access GUI for copy/paste
Cntrl 0, Enter, cntrl X to save the file and x for exit :)
docker-compose -f docker-compose.prod.yml up -d

#### adding GUI (optional)
Web-Base File Manager
sudo apt install cockpit -y
sudo systemctl enable --now cockpit
https://YOUR_SERVER_IP:9090
---
sudo systemctl start cockpit
systemctl status cockpit
sudo systemctl enable cockpit