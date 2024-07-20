pip install alembic
echo "gotten alembic"
pip install -r requirements.txt
python manage.py collectstatic --noinput
