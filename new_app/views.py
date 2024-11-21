from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from new_app.models import Enquiry


#
# class SnippetList(generics.ListCreateAPIView):
#     queryset = Enquiry.objects.all()
#     serializer_class = Enquiry_serializer


# views.py
import gspread
from google.oauth2.service_account import Credentials
from rest_framework.response import Response
from rest_framework import status, views

from django.conf import settings

from new_app.serializer import EnquirySerializer

import gspread
from google.oauth2.service_account import Credentials
from rest_framework.response import Response
from rest_framework import status, views

from django.conf import settings

from google.oauth2.service_account import Credentials
import gspread
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status, views
from new_app.serializer import EnquirySerializer


class EnquiryToGoogleSheetView(views.APIView):
    def post(self, request):
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
            # Build credentials from environment variables
            creds = Credentials.from_service_account_info(
                {
                    "type": "service_account",
                    "project_id": settings.GOOGLE_PROJECT_ID,
                    "private_key_id": settings.GOOGLE_PRIVATE_KEY_ID,
                    "private_key": settings.GOOGLE_PRIVATE_KEY,
                    "client_email": settings.GOOGLE_CLIENT_EMAIL,
                    "client_id": settings.GOOGLE_CLIENT_ID,
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                    "client_x509_cert_url": f"https://www.googleapis.com/robot/v1/metadata/x509/{settings.GOOGLE_CLIENT_EMAIL}",
                },scopes=SCOPES
            )

            # Authorize and open the Google Sheet
            client = gspread.authorize(creds)
            sheet = client.open_by_key(settings.GOOGLE_SHEET_ID).sheet1

            # Append the data
            sheet.append_row([
                serializer.validated_data['name'],
                serializer.validated_data['phone'],
                serializer.validated_data['email'],
            ])

            return Response({"message": "Enquiry saved to Google Sheet"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class EnquiryToGoogleSheetView(views.APIView):
#     def post(self, request):
#         # Serialize data
#         serializer = EnquirySerializer(data=request.data)
#         if serializer.is_valid():
#             # Define the Google Sheets API scope
#             SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
#
#             # Authenticate with the correct scope and open Google Sheet
#             creds = Credentials.from_service_account_file(
#                 settings.GOOGLE_SHEETS_CREDS, scopes=SCOPES
#             )
#             client = gspread.authorize(creds)
#             sheet = client.open_by_key(settings.GOOGLE_SHEET_ID).sheet1  # or specify sheet name if not sheet1
#
#             # Extract data from the validated serializer
#             name = serializer.validated_data['name']
#             phone = serializer.validated_data['phone']
#             email = serializer.validated_data['email']
#
#             # Append row to Google Sheet
#             sheet.append_row([name, phone, email])
#
#             return Response({"message": "Enquiry saved to Google Sheet"}, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

