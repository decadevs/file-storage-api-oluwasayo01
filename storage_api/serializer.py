from django_restframework import serializer
from storage_api.models import Bucket

class BucketSerializer(serializer.ModelSerializer):
    class Meta:
        model = Bucket
        fields = '__all__'