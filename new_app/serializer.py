from rest_framework import serializers

from new_app.models import Enquiry


# class Enquiry_serializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Enquiry
#         fields = '__all__'


class EnquirySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    phone = serializers.CharField(max_length=50)
    email = serializers.EmailField()