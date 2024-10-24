from rest_framework import viewsets
from .serializers import permissionserializer
from .models import permission
class permissionviewset(viewsets.ModelViewSet):
	queryset=permission.objects.all()
	serializer_class=permissionserializer