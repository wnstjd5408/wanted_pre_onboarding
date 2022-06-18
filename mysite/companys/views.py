from config.permissions import IsStaffOrReadOnly
from rest_framework import permissions, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Company, Job_Posting
from .serializers import CompanySerializer, JobPostingSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    permission_classes = [IsStaffOrReadOnly, IsAuthenticatedOrReadOnly]


# Create your views here.
class JobPostringViewSet(viewsets.ModelViewSet):
    serializer_class = JobPostingSerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_queryset(self):
        return Job_Posting.objects.filter(company=self.kwargs["company_pk"])
