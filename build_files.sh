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
python3 manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="${DJANGO_SUPERUSER_USERNAME}").exists():
    User.objects.create_superuser(
        username="admin",
        email="admin",
        password="admin.com"
    )
EOF
# echo "from django.contrib.auth.models import User; User.objects.create_superuser('Mr-Ken', 'admin@gmail.com', 'NOvendd7.com')" | python3 manage.py shell

echo "Build process completed successfully."
