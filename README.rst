Seguros 2020
==============

How to install
--------------

::
    git clone git@github.com:joaquinquintas/seguros2020.git
    sudo docker-compose -f local.yml build
    sudo docker-compose -f local.yml run django manage.py migrate
    sudo docker-compose -f local.yml run django manage.py createsuperuser
    sudo docker-compose -f local.yml up
