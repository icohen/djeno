python manage.py reset_db --router=default --noinput
python manage.py syncdb --noinput
python manage.py loaddata geno
