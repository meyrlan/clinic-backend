release: python www/manage.py migrate
web: gunicorn --chdir www config.wsgi:application && cd www
