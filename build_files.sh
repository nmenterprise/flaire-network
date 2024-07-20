pip3 install alembic
echo "gotten alembic"
pip3 install -r requirements.txt
python3 manage.py collectstatic --noinput
