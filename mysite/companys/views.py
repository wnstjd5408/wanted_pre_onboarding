from config.permissions import IsStaffOrReadOnly
from rest_framework import permissions, viewsets
from rest_framework.filters import SearchFilter
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
    filter_backends = [SearchFilter]
    search_fields = ["jp_technology"]

    def get_queryset(self):
        return Job_Posting.objects.filter(company=self.kwargs["company_pk"])

    # def perform_create(self, serializer):
    #     serializer.save(company=self.kwargs["company_pk"])


class JobPostingAllViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Job_Posting.objects.all()
    serializer_class = JobPostingListSerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [SearchFilter]

    search_fields = ["company__cp_name", "jp_technology"]
