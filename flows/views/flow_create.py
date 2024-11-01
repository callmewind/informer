from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView

from accounts.mixins import CurrentEnvironmentMixin
from flows.forms import FlowForm


class FlowCreate(CurrentEnvironmentMixin, CreateView):
    form_class = FlowForm

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(
            reverse("flows:list", kwargs={
                    "environment": self.current_environment.slug})
        )

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.site = self.request.site
        self.object.user = self.request.user
        self.object.save()
        self.object.environments.add(self.current_environment)
        messages.success(
            self.request, _(
                "%(name)s was created successfully") % form.cleaned_data
        )
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, **kwargs):
        messages.error(self.request, "Error creating flow")
        return HttpResponseRedirect(
            reverse("flows:list", kwargs={
                    "environment": self.current_environment.slug})
        )

    def get_success_url(self):
        return reverse(
            "flows:edit",
            kwargs={"id": self.object.id,
                    "environment": self.current_environment.slug},
        )
