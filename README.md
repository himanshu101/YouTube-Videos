# Youtube-Restful-API's  

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists. (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs.
* Mysql

## Installation for linux
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can run this:
    ```bash
        $ apt-get update
        $ apt-get install -y python3-dev python-pip
    ```
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/SigtupleTechnologies/lis.git
    ```

* #### Dependencies
  ##### First Method
    1. Copy env file and change according to your system
        ```bash
            $ cp .env.example .env
        ```
    2. Cd into your the cloned repo as such:
        ```bash
            $ cd fampayassignment
        ```
    3. Create and fire up your virtual environment:
        ```bash
            $ virtualenv venv -p python3
            $ source venv/bin/activate
        ```
    4. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    
    5. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

  #### Second Method(Using docker)
    1. Perform Step 1, 2, 3 and 5 to add .env file and run migrations as mentioned in the First Method.
    
    2. Run Following Commands:
        ```bash
            $ docker-compose build
       ```

* #### Run It
    Fire up the server using following methods:
    1. Using Running Server
    ```bash
        $ python manage.py runserver
    ```
    2. Using Docker Image:
    ```bash
        $ docker-compose up -d
    ```
    
    ##### You can now access the api service on your browser by using
    ```
        http://localhost:8000/api/v1/videos
    ```

* #### Add Crons
    1. Adding example to add cron by running following command in terminal:
    ```bash
            $ crontab -e
    ```
  
    2. Add path of Django project. Adding example.
    ```bash
        */1 * * * * cd /Users/himanshugarg/IdeaProjects/fampayassignment && source /Users/himanshugarg/IdeaProjects/fampayassignment/venv/bin/activate && /Users/himanshugarg/IdeaProjects/fampayassignment/venv/bin/python /Users/himanshugarg/IdeaProjects/fampayassignment/src/locallibrary/manage.py runcrons > /tmp/cronjob.log 2>&1
    ```
  
