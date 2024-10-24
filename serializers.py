from rest_framework import serializers
from .models import permission
class permissionserializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=permission
		fields=('Name','Roll_No','E_Mail','Department','Club_Name','Achivement_in_Club','Certificate')