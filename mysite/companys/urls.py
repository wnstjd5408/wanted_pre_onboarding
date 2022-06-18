from django.urls import include, path
from rest_framework_nested import routers

from .views import CompanyViewSet, JobPostingViewSet

router = routers.DefaultRouter()


router.register(r"", CompanyViewSet, basename="company")
job_posting_router = routers.NestedDefaultRouter(router, "", lookup="company")
job_posting_router.register("job_postings", JobPostingViewSet, basename="job_posting")


urlpatterns = [
    path("", include(router.urls)),
    path("", include(job_posting_router.urls)),
]
