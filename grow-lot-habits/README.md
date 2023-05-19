1. docker-compose build
2. docker-compose up
Now you have to run appscheduler for sending reminders by appscheduler:
3. Find running docker containers using the 'docker ps' command. Note the name.
4. Use the name of the container to login to it: 'docker exec -it NAME_OF_CONTAINER bash'
5. Run the command:
 $ cd /project
 $ python manage.py runapscheduler