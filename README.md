## Djeno - genealogy in Django

Disclaimer: This is 100% my wife [@heathercolson](http://twitter.com/heathercolson)'s idea. Heather started this as her first Django project and I stole it to experiment and prove my Django prowess. 

### Prerequesities  
-mysql with user root and blank password

-mysql database named djeno

    (ugc)ugc $ mysql -uroot 
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 1291
    Server version: 5.1.55 Source distribution
    
    mysql> create database django_ugc;
    Query OK, 1 row affected (0.00 sec)

-virtual env or clean python site packages on a fresh VM

### Install Requirements
    (djeno)djeno $ pip install -r requirements.txt 

### Create db, sync initial data, and run dev server
    (djeno)djeno $ bin/reset-db.sh 
    Creating tables ...
    Creating table auth_permission
    Creating table auth_group_permissions
    Creating table auth_group
    Creating table auth_user_user_permissions
    Creating table auth_user_groups
    Creating table auth_user
    Creating table django_content_type
    Creating table django_session
    Creating table django_site
    Creating table django_admin_log
    Creating table geno_person_siblings
    Creating table geno_person
    Creating table geno_event
    Creating table geno_birth
    Creating table geno_death
    Creating table geno_spouse
    Creating table geno_marriage
    Installing custom SQL ...
    Installing indexes ...
    Installed 2 object(s) from 1 fixture(s)
    Installed 23 object(s) from 1 fixture(s)

    
    (djeno)djeno $ bin/start-dev.sh 
    Validating models...

    0 errors found
    Django version 1.4c1, using settings 'djeno.settings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    
    