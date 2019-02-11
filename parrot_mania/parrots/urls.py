from rest_framework import routers

from parrots.views import ParrotViewSet


router = routers.SimpleRouter()
router.register(r'parrots', ParrotViewSet, base_name='parrots')
urlpatterns = router.urls
