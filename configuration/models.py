from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType

class Account(models.Model):
    name = models.CharField(_('name'), max_length=50)

    def __str__(self):
        return self.name


class Environment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name=_('account'), editable=False, related_name='environments')
    name = models.CharField(_('name'), max_length=50, unique=True)
    slug = models.SlugField(_('slug'), editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(**kwargs)


class Channel(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name=_('account'), editable=False)
    name = models.CharField(_('name'), max_length=100)
    enabled = models.BooleanField(_('enabled'), default=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, editable=False)

    def get_typed_instance(self):
        return getattr(self, self.content_type.model)

    def __str__(self):
        return self.get_typed_instance().__str__()


    def save(self, *args, **kwargs):
        if not self.content_type_id:
            content_type = ContentType.objects.get_for_model(self, for_concrete_model=True)
            if content_type.model_class() != Channel:
                self.content_type = content_type
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('account', 'name',)
        verbose_name = _('channel')
        verbose_name_plural = _('channels')
        unique_together = ('account', 'name')

    def __str__(self):
        return self.name


class EmailChannel(Channel):
    host = models.CharField(_('host'), max_length=100)
    port = models.PositiveSmallIntegerField(_('port'))
    username = models.CharField(_('username'), max_length=150)
    password = models.CharField(_('password'), max_length=150)

    class Meta:
        verbose_name = _('email channel')
        verbose_name_plural = _('email channels')