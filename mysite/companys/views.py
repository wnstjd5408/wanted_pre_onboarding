from config.permissions import IsStaffOrReadOnly, IsUserOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework import permissions, status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Apply, Company, Job_Posting
from .serializers import ApplySerializer, CompanySerializer, JobPostingListSerializer, JobPostingSerializer


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


class ApplyViewSet(viewsets.ModelViewSet):
    serializer_class = ApplySerializer
    permission_classes = [IsUserOrReadOnly, permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Apply.objects.filter(user=user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        apply = Apply.objects.filter(user=self.request.user)

        if serializer.is_valid(raise_exception=True) and len(apply) == 0:
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
