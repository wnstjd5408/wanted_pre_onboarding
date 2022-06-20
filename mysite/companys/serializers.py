from calendar import c
from dataclasses import fields

from rest_framework import serializers
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

from .models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


# class JobPostingSerializer(NestedHyperlinkedModelSerializer):
#     parent_lookup_kwarg = {"company_pk": "company__pk"}
#     company = CompanySerializer(read_only=True)

#     class Meta:
#         model = Job_Posting
#         fields = ("id", "jp_position", "jp_content", "jp_compensation", "jp_technology", "company")

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         company_representation = representation.pop("company")
#         for key in company_representation:
#             representation[key] = company_representation[key]

#         return representation


class JobPostingListSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Job_Posting
        fields = ("id", "jp_position", "jp_compensation", "jp_technology", "company")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        company_representation = representation.pop("company")
        for key in company_representation:
            representation[key] = company_representation[key]

        return representation

    def create(self, validated_data):
        comapany = validated_data.pop("company")
        jobposting_instance = Job_Posting.objects.create(**validated_data)
        for cp in comapany:
            Company.objects.create(**cp)
        return jobposting_instance


class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Posting
        fields = ("jp_position", "jp_compensation", "jp_content", "jp_technology", "company")
        read_only_fields = ("company",)

    # def to_internal_value(self, data):
    #     company_internal = {}
    #     for key in CompanySerializer.Meta.fields:
    #         if key in data:
    #             company_internal[key] = data.pop(key)

    #     internal = super().to_internal_value(data)
    #     internal["company"] = company_internal
    #     return internal


class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = ("job_posting", "user")
