from config.permissions import IsStaffOrReadOnly
from rest_framework import permissions, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Company, Job_Posting
from .serializers import CompanySerializer, JobPostingListSerializer, JobPostingSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    permission_classes = [IsStaffOrReadOnly, IsAuthenticatedOrReadOnly]


# Create your views here.
class JobPostingViewSet(viewsets.ModelViewSet):
    serializer_class = JobPostingSerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_queryset(self):
        return Job_Posting.objects.filter(company=self.kwargs["company_pk"])

    # def perform_create(self, serializer):
    #     serializer.save(company=self.kwargs["company_pk"])


class JobPostingAllViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JobPostingListSerializer
    permission_classes = [IsStaffOrReadOnly]
    queryset = Job_Posting.objects.all()
