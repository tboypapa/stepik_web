sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo pip3 install gunicorn==17.5
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test-django
sudo /etc/init.d/gunicorn restart
~/web/ask/manage.py makemigrations qa
~/web/ask/manage.py migrate qa