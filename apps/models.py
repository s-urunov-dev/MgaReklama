from django.db.models import Model, ImageField, DateTimeField, CharField, EmailField, URLField, TextField
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Banner(Model):
    image = ImageField(upload_to='banner', verbose_name=_("Image"))

    class Meta:
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")


class Gallery(Model):
    image = ImageField(upload_to='images/%Y/%m/%d', verbose_name=_("Image"))
    created = DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Galleries")


class SiteSetting(Model):
    phone_number = CharField(max_length=11, verbose_name=_("Phone Number"))
    email = EmailField(max_length=100, verbose_name=_("Email"))
    address = CharField(max_length=120, verbose_name=_("Address"))
    banner = ImageField(upload_to='banner/%Y/%m/%d', verbose_name=_("Banner Image"))
    text = TextField(verbose_name=_("Text"))
    instagram = CharField(max_length=120, verbose_name=_("Instagram"))
    facebook = CharField(max_length=120, verbose_name=_("Facebook"))
    youtube = CharField(max_length=120, verbose_name=_("YouTube"))
    telegram = CharField(max_length=120, verbose_name=_("Telegram"))

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Site Setting")
        verbose_name_plural = _("Site Settings")


class ContactForm(Model):
    name = CharField(max_length=100, verbose_name=_("Name"))
    email = EmailField(max_length=100, verbose_name=_("Email"))
    phone = CharField(max_length=12, verbose_name=_("Phone Number"))
    subject = CharField(max_length=100, verbose_name=_("Subject"))
    message = TextField(verbose_name=_("Message"))
    created = DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    class Meta:
        verbose_name = _("Contact Form")
        verbose_name_plural = _("Contact Forms")




class Partner(Model):
    image = ImageField(upload_to='partners/%Y/%m/%d', verbose_name=_("Image"))
    url = URLField(max_length=100, verbose_name=_("URL"), null=True, blank=True)

    class Meta:
        verbose_name = _("Partner")
        verbose_name_plural = _("Partners")

    def __str__(self):
        return self.url


class Service(TranslatableModel):
    translations = TranslatedFields(
        title = CharField(max_length=120, verbose_name=_("Title"))
    )

    image = ImageField(upload_to='services-icon/%Y/%m/%d', verbose_name=_("Icon"), null=True, blank=True)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")




class ClientComment(Model):
    avatar = ImageField(upload_to='reviews/%Y/%m/%d', verbose_name=_("Avatar"))
    full_name = CharField(max_length=120, verbose_name=_("Full Name"))
    job = CharField(max_length=120, verbose_name=_("Job Title"))
    description = TextField(verbose_name=_("Description"))

    class Meta:
        verbose_name = _("Client Comment")
        verbose_name_plural = _("Client Comments")
