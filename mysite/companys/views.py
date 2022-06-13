from config.permissions import IsUserOrReadOnly
from rest_framework import permissions, viewsets

from .models import Company, Job_Posting
from .serializers import CompanySerializer, JobPostingSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    permission_classes = [permissions.AllowAny]


# Create your views here.
class JobPostringViewSet(viewsets.ModelViewSet):
    queryset = Job_Posting.objects.all()
    serializer_class = JobPostingSerializer
