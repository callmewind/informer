from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager


class Channel(models.Model):
    objects = CurrentSiteManager
    site = models.ForeignKey(Site, verbose_name=_('site'), on_delete=models.CASCADE, related_name='channels')
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
        ordering = ('site', 'content_type',)
        verbose_name = _('channel')
        verbose_name_plural = _('channels')
        unique_together = ('site', 'content_type',)

    def __str__(self):
        return self.content_type.name
