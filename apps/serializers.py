from rest_framework.serializers import ModelSerializer, CharField

from apps.models import Gallery, SiteSetting, Partner, Service, ContactForm, ClientEmail


class ImageModelSerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class SiteSettingSerializer(ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = '__all__'


class PartnerModelSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class ServiceModelSerializer(ModelSerializer):
    title = CharField(read_only=True)

    class Meta:
        model = Service
        fields = 'title', 'image'


class ContactFormModelSerializers(ModelSerializer):
    class Meta:
        model = ContactForm
        exclude = 'created',


class ClientEmailModelSerializers(ModelSerializer):
    class Meta:
        model = ClientEmail
        fields = '__all__'
