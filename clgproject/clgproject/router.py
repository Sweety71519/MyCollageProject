from master import views
from rest_framework import routers
from django.urls import path,include



router=routers.DefaultRouter()
router.register(r'master',views.SnippetViewSets)


urlpatterns = [
    path('',include(router.urls))
    # path('/', include('rest_framework.urls'))
]