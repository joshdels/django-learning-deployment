# django-learning-deployment

Practice repository for deploying Django applications using Docker.

## How I Learn
1. Shortcuts – memorize commands and workflows.
2. Official documentation – reference Django, Docker, etc.
3. Source code – explore for deeper understanding.

---

## Docker Setup

**Installation:**
1. Install Ubuntu.
2. Configure WSL2 (if using Windows).
3. Open Docker Desktop.

**Key Files:**
- Dockerfile – defines Docker image.
- docker-compose.yml – manages containers.
- .dockerignore – excludes files from build.

**Common Commands:**
docker build .
docker-compose up
docker-compose up -d       # Detached mode
docker-compose exec [service] [command]
docker-compose down
docker-compose

**Security:**
docker-compose exec web python -c "import secrets; print(secrets.token_urlsafe(38))"
docker-compose exec web python manage.py check --deploy

**Remove Images:**
docker system prune -f
docker-compose build --no-cache

---

## Django Notes
1. User Models:
   - AbstractUser – minimal customization
   - AbstractBaseUser – full manual setup
2. Static Files: collectstatic for production (STATIC_ROOT, STATICFILES_DIRS)
3. Use django-allauth for authentication
4. Deployment workflow:
   - Local: docker-compose.yml
   - Production: docker-compose.prod.yml

---

## Deploying to Vultr VPS

**SSH to Server:**
ssh root@YOUR_SERVER_IP

**Install Docker:**
sudo apt update && sudo apt upgrade -y
sudo apt install -y docker.io docker-compose
sudo systemctl enable docker
sudo systemctl start docker
docker --version
docker-compose --version

**Run Django App:**

*From Git:*
sudo apt install -y git
git clone https://github.com/USERNAME/REPO_NAME.git /root/myapp
cd /root/myapp
docker-compose up -d

*From Local Machine:*
scp -r ./myapp root@YOUR_SERVER_IP:/root/myapp

**Add Production Keys:**
cd /root/myapp
nano docker-compose.prod.yml
docker-compose -f docker-compose.prod.yml up -d

---

## Optional Web-Based GUI
sudo apt install cockpit -y
sudo systemctl enable --now cockpit
# Access via: https://YOUR_SERVER_IP:9090

---
## Connecting your Domain to your Server 
**Domain** 
Add your server IP 

**Server Setup 1. Add SSL with** 
sudo apt update
sudo apt install nginx
sudo apt install certbot python3-certbot-nginx

**Open Ports**
ping topmapsolutions.com (should redirect to your server ip)
sudo ufw allow 80
sudo ufw allow 443
sudo ufw reload
sudo ufw status
sudo certbot --nginx -d topmapsolutions.com -d www.topmapsolutions.com
docker-compose up --build