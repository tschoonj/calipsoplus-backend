from django.conf.urls import url, include
from django.urls import path

from apprest.views.experiment import GetExperimentsByUserName
from apprest.views.facility import GetAllFacilities
from apprest.views.favorite import CalipsoExperimentFavorite
from apprest.views.image import GetUsedQuotaFromUser, GetInfoImage
from apprest.views.login import login_user, logout_user, get_calipso_settings
from apprest.views.quota import GetDefaultUserQuotasFromUser

urlpatterns = [
    url(r'^container/', include('apprest.urls.container')),
    url(r'^umbrella/', include('apprest.urls.umbrella')),
    path('experiments/<username>/', GetExperimentsByUserName.as_view()),
    url(r'^favorite/(?P<pk>[0-9]+)/$', CalipsoExperimentFavorite.as_view()),
    path('quota/<username>/', GetDefaultUserQuotasFromUser.as_view()),
    path('used_quota/<username>/', GetUsedQuotaFromUser.as_view()),
    path('image/<public_name>/', GetInfoImage.as_view()),
    path('facility/', GetAllFacilities.as_view()),
    path('login/', login_user),
    path('logout/', logout_user),
    path('settings/', get_calipso_settings),
]