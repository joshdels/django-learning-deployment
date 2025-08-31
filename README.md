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

### deploying for heroku (note must create account first)
heroku login
- setup
- build
- release 
- run
heroku create
add Django Secret KEY
heroku stack:set container -a cryptic-shore-97883
heroku addons:create --> for adding services/tier level
heroku git:remote -a cryptic-shore-97883
git push heroku main
# add
'''if it  ask for credentials, type this'''
email - heroku email
pass - (heroku auth:token)