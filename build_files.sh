pip3 install django>=3.0,<4.0
pip3 install whitenoise
pip3 install channels
pip3 install daphne
pip3 install python-decouple
pip3 install psycopg2-binary
echo "gotten alembic"
python3 manage.py collectstatic --noinput
