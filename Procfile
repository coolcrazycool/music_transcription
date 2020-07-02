release: docker-compose -f docker-compose.yml up -d --build
release: docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput
web: gunicorn hyper_music.wsgi
