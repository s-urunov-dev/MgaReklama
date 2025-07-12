from django.urls import path

from apps.views import GalleryListAPIView, SiteSettingView, PartnerListAPIView, ServiceListAPIView, \
    ContactFormCreateAPIView

urlpatterns = [
    path('images/', GalleryListAPIView.as_view()),
    path('site-setting/', SiteSettingView.as_view()),
    path('partners/', PartnerListAPIView.as_view()),
    path('services/', ServiceListAPIView.as_view()),
    path('create-contact/', ContactFormCreateAPIView.as_view()),
]