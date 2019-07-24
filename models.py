from django.db import models

# Create your models here.
class Merchandiser(models.Model):
	full_name = models.CharField(max_length=25)
	store_name = models.CharField(max_length=25)
	address = models.CharField(max_length=500)
	zip_code = models.IntegerField(default=4)
	phone_no = models.IntegerField(default=11)
	tin_no = models.IntegerField(default=19)
	birth_of_date = models.DateTimeField()
	optional_website = models.TextField(max_length=100)
	password = models.CharField(max_length=50)
	c_password = models.CharField(max_length=50)

python manage.py makemigrations Merchandiser