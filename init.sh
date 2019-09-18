sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo pip3 install --upgrade django
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test-django
sudo gunicorn -c /etc/gunicorn.d/test-django ask.wsgi:application
sudo /etc/init.d/gunicorn restart