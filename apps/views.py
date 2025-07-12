from django.utils import translation
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from apps.models import Gallery, SiteSetting, Partner, Service, ContactForm, ClientEmail
from apps.serializers import ImageModelSerializer, SiteSettingSerializer, PartnerModelSerializer, \
    ServiceModelSerializer, ContactFormModelSerializers, ClientEmailModelSerializers


class GalleryListAPIView(ListAPIView):
    queryset = Gallery.objects.order_by('-id')
    serializer_class = ImageModelSerializer


class SiteSettingView(RetrieveAPIView):
    queryset = SiteSetting.objects.all()
    serializer_class = SiteSettingSerializer

    def get_object(self):
        return SiteSetting.objects.get_or_create(pk=1)[0]


class PartnerListAPIView(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerModelSerializer

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

@extend_schema(
    parameters=[
        OpenApiParameter(
            name='lang',
            type=OpenApiTypes.STR,
            location=OpenApiParameter.HEADER,
            required=False,
            description='Language code (en, ru)'
        )
    ]
)
class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceModelSerializer

    def get_queryset(self):
        lang = self.request.headers.get('lang') or 'en'
        translation.activate(lang)
        self.request.LANGUAGE_CODE = lang

        queryset = super().get_queryset()
        return queryset.active_translations(lang)


class ContactFormCreateAPIView(CreateAPIView):
    model = ContactForm
    serializer_class = ContactFormModelSerializers


class EmailCreateAPIView(CreateAPIView):
    model = ClientEmail
    serializer_class = ClientEmailModelSerializers
