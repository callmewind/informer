from uuid import uuid4 
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Flow(models.Model):
    id = models.UUIDField(_('id'), default=uuid4, editable=False)
    revision = models.UUIDField(_('revision'), primary_key=True, default=uuid4, editable=False)
    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, verbose_name=_('account'), editable=False)
    date = models.DateTimeField(_('date'), auto_now_add=True)
    environments = models.ManyToManyField('accounts.Environment', related_name='flows', editable=False)
    name = models.CharField(_('name'), max_length=150)
    enabled = models.BooleanField(_('enabled'), default=True)
    trigger = models.CharField(_('trigger'), max_length=150, db_index=True)
    user = models.ForeignKey('accounts.user', on_delete=models.PROTECT, verbose_name=_('user'), editable=False)
    
    def save(self, *args, **kwargs):
        steps = list(self.steps.all())
        self.pk = uuid4()
        self._state.adding = True
        super().save(**kwargs)
        for step in steps:
            # We need to call save() from the child class
            step = step.get_typed_instance()
            step.flow = self
            step.save(*args, **kwargs)

    def __str__(self):
        return self.name        

    class Meta:
        verbose_name = _('flow')
        verbose_name_plural = _('communication flows')
        ordering = ('id', '-date')
        unique_together = ('id', 'date')