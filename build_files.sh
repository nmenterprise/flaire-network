pip3 install django
pip3 install whitenoise
pip3 install channels
pip3 install daphne
pip3 install python-decouple
pip3 install psycopg2-binary
echo "gotten alembic"
python3 manage.py collectstatic --noinput
python3 manage.py makemigrations
python3 manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('Mr-Ken', 'admin@gmail.com', 'NOvendd7.com')" | python3 manage.py shell

echo "Build process completed successfully."
daphne -b 0.0.0.0 -p 8000 flare-network.asgi:application
