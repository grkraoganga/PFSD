from django.urls import path
from . import views
urlpatterns = [
    path("ttmhome",views.ttmhome,name="ttmhome"),
    path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
    path("checkregistration",views.checkregistration,name="checkregistration"),
    path("EditPackage",views.editpackage,name="package"),
    path("checkpackage",views.checkpackage,name="checkpackage"),
    path("changepasswd",views.checkchangepasswd,name="changepasswd"),
    path("viewplaces",views.viewplaces,name="viewplaces"),
]