from django.contrib import admin
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.urls import reverse
from parler.admin import TranslatableAdmin

from apps.models import Gallery, SiteSetting, ContactForm, Partner, Service, ClientEmail


@admin.register(Gallery)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(SiteSetting)
class SiteSettingsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        if SiteSetting.objects.exists():
            obj = SiteSetting.objects.first()
            return redirect(reverse('admin:apps_sitesetting_change', args=[obj.id]))
        return super().changelist_view(request, extra_context)

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = 'name', 'email', 'phone'
    search_fields = 'name', 'email', 'phone'


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    pass


@admin.register(Service)
class ServiceTranslatableAdmin(TranslatableAdmin):
    list_display = 'title',


@admin.register(ClientEmail)
class ClientEmailModelAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
