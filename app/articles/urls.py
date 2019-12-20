from rest_framework.routers import SimpleRouter

from .views import ArticleViewSet
 

app_name = 'articles' 

router = SimpleRouter()
router.register(
    prefix=r'',
    basename='articles',
    viewset=ArticleViewSet
)
urlpatterns = router.urls