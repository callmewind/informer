from django.db import models
from django.utils.translation import gettext_lazy as _
from .pipeline_step import PipelineStep

class Delay(PipelineStep):
	time = models.DurationField(_('time'))
