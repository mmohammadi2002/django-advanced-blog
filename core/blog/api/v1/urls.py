from rest_framework.routers import SimpleRouter

from . import views

app_name = "api-v1"

router = SimpleRouter()
router.register(
    "post",
    views.PostModelViewSet,
    basename="post",
)
router.register(
    "category",
    views.CategoryModelViewSet,
    basename="category",
)

urlpatterns = router.urls
