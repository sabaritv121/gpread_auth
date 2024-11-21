from django.urls import path


from new_app.views import EnquiryToGoogleSheetView

urlpatterns = [
   # path("enquiry_form",views.SnippetList.as_view()),

    path("enquiry/",EnquiryToGoogleSheetView.as_view(), name="enquiry-to-google-sheet"),


]