# mysite_0412

git clone https://github.com/g00u00/mysite_0412.git

или

git init

git remote add origin git@github.com:g00u00/mysite_0412.git

git pull origin main

cd mysite_0412

python3 -m venv env

. env/bin/activate

pip install -r requirements.txt

python manage.py runserver 10.0.2.15:8000

admin root root

deactivate

------------

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8000

-------------=

pip freeze > requirements.txt

pip install -r requirements.txt

--------------------

https://www.djbook.ru/rel1.8/ref/models/

https://docs.djangoproject.com/en/4.0/topics/db/models/

https://docs.djangoproject.com/en/4.0/ref/models/
