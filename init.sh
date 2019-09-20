sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo pip3 install gunicorn==17.5
python3 ~/web/ask/manage.py makemigrations qa
python3 ~/web/ask/manage.py migrate qa
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test-django
sudo /etc/init.d/gunicorn restart
cd web/ask
sudo gunicorn --bind 0.0.0.0:8000 ask.wsgi:application &
curl localhost:8000