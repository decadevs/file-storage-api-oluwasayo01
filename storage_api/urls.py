from rest_framework import routers
from .api import BucketViewSet

router = routers.DefaultRouter()
router.register('api/objects',  BucketViewSet,  'buckets')
urlpatterns = router.urls 