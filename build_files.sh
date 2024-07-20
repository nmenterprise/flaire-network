python3 -m venv venv
source venv/bin/activate
pip install alembic
echo "gotten alembic"
pip install -r requirements.txt
python3 manage.py collectstatic --noinput
