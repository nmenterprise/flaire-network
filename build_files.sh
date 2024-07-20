pip3 install alembic
pip3 install binwalk
echo "gotten alembic"
pip3 install -r requirements.txt
python3 manage.py collectstatic --noinput
