python3 -m venv venv
source venv/bin/activate
pip install alembic
pip install -r requirements.txt
python3 manage.py collectstatic --noinput
