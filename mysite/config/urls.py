"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from companys.serializers import ApplySerializer
from companys.views import ApplyViewSet, JobPostingAllViewSet
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"applys", ApplyViewSet, basename="apply")
router.register(r"job_postings", JobPostingAllViewSet, basename="job_postings")
urlpatterns = [
    path("admin/", admin.site.urls),
    path("companys/", include("companys.urls")),
    path("", include(router.urls)),
]
