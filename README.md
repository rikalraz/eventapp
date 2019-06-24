# Events app in Flask

#### Online Demo in Heroku
https://myriadeventapi.herokuapp.com

#### Technology stack 
| Name | Version |
| ------ | ------ |
| Python | 3.7.3 |
| Flask	| 4.0 | 
| MongoDB |  3.11.0 | 
| Angular |  8.0.3 | 


#### Setup locally
##### Start backend server
1. clone repository,
2. install virtualenv,
3. cd path/to/repo,
4. Start virtual env
    venv/bin/activate or source bin/activate
5. pip install flask
    Install these dependencies as well: pymongo, dnspython, Flask-Cors, gunicorn, pymongo, virtualenv, virtualenvwrapper-win and other dependencies may also require
6. Flask api server will now serve from localhost:5000, from your web browser some get methods like http://localhost:5000/v1/api/events can be accessible.

##### Start frontend 
1. Go to frontend folder inside the,
2. install the npm package,
    ```sh
    $ npm install
    ```
3. start the ng server
    ```sh
    $ ng serve
    ```
    
#### Deploy to remote server
1. Build angular app to production, 
     ```sh
    $ ng build --prod
    ```
2. Copy everything within the output folder (dist/ by default) to a folder on the server.
3. Configure your mongodb server 
4. Setup your flask project 
(Install to remote server differs, follow as per the service requirement)