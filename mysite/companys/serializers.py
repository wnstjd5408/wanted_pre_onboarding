from rest_framework import serializers

from .models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class JobPostingSerializer(serializers.ModelSerializer):
    # company_info = CompanySerializer()

    class Meta:
        model = Job_Posting
        fields = ("jp_position", "jp_content", "jp_compensation", "jp_technology", "company")
