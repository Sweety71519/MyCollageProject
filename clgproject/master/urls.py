from django.urls import path,include
from master.views import *
from master import zoneview
from master import stateview
from master import areaview
from master import districtview
from master import cityview
from master import userview
from master import loginview
from master import productview
from rest_framework import routers

from rest_framework import urls

router=routers.DefaultRouter()

#router.register('login', userview.LoginView)
# routes = router.get_routes(userview.Login)

# viewset_class = userview.Login
# viewset = viewset_class()
# routes = router.get_routes(viewset_class)


router.register(r'master',SnippetViewSets)
router.register(r'country',CountryViewSets)
router.register(r'zone',zoneview.ZoneViewSets)
router.register(r'state',stateview.StateViewSets)
router.register(r'area',areaview.AreaMasterViewSets)
router.register(r'district',districtview.DistrictViewSets)
router.register(r'city',cityview.CityViewSets)
router.register(r'product',productview.ProductViewSets)
router.register(r'user',userview.UserinformationViewSets)

router.register(r'zonedata',zoneview.ZoneDataByCountry,basename='Zone')
router.register(r'statedata',stateview.StateDataByCountry,basename='State')
#router.register(r'login', loginview.LoginView.as_view())

# router.register('login', userview.Login, basename='login')
#router.register(r'login',loginview.LoginView)

#router.register(r'/data/',MySnippetFillterData)

urlpatterns = [
    path('',include(router.urls))
    # path('snippets/', snippet_list),
    # path('snippets/<int:pk>/',snippet_detail),
    # path('',hello,name='hello'),
]
