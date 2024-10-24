from django.db import models
class permission(models.Model):
	Name=models.CharField(max_length=50)
	Roll_No=models.FloatField(max_length=50)
	E_Mail=models.EmailField()
	Department=models.CharField(max_length=40)
	Club_Name=models.CharField(max_length=40)
	Achivement_in_Club=models.TextField(max_length=40)
	Certificate=models.FileField(upload_to='files/')
