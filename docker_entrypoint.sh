echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@admin.com','Kakbir19.' )" | python manage.py shell

echo "Look Makemigrations"
python manage.py makemigrations

echo "Start Migrate"
python manage.py migrate

echo "Start Server"
#python manage.py runserver 0.0.0.0:8000
python manage.py runsslserver 0.0.0.0:8000 --certificate cert.pem --key key.pem