pip3 install django
pip3 install whitenoise
pip3 install channels
pip3 install daphne
echo "gotten alembic"
pip3 install -r requirements.txt
python3 manage.py collectstatic --noinput
