echo "BUILD START"

python3.9 -m pip install --upgrade pip
# create a virtual environment named 'venv' if it doesn't already exist
python3.9 -m venv venv

# activate the virtual environment
source venv/bin/activate


# install all deps in the venv
pip install -r requirement.txt

# collect static files using the Python interpreter from venv
/vercel/path0/venv/bin/python3.9 manage.py collectstatic --noinput

# /vercel/path0/venv/bin/python3.9 manage.py runserver

echo "BUILD END"

# [optional] Start the application here 
# python manage.py runserver
