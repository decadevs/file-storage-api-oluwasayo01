from rest_framework import viewsets, permissions
from .serializer import BucketSerializer
from storage_api.models import Bucket 

class BucketViewSet(viewsets.ModelViewSet):
    queryset = Bucket.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = BucketSerializer