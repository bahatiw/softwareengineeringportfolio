"# softwareengineeringportfolio" 
installation
- You can unzip the file of clone it from Git hub
Installing from zip file

Installing from Git Hub
git clone https://github.com/bahatiw/softwareengineeringportfolio.git
cd  cd .\softwareengineeringportfolio\
# To create and initialize the database run
docker-compose run web python manage.py migrate
# Lets insert some dummy variables 
docker-compose run web python createdummydata.py
# Finally we fire the application
 docker-compose up

# Access the application via the browser at
http://127.0.0.1:8000/

# To access Djabgo admin interface. first create super user
docker-compose run web python manage.py createsuperuser
# Access the admin interface via
http://127.0.0.1:8000/admin/