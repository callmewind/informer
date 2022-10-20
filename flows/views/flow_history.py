from django.views.generic.list import ListView
from accounts.views import CurrentEnvironmentMixin
from flows.models import Flow, FlowStep
from django.db.models import Prefetch

class FlowHistory(CurrentEnvironmentMixin, ListView):
    template_name_suffix = '_history'
    model = Flow
    def get_queryset(self):
        return super().get_queryset().filter(
            id=self.kwargs['id'], account=self.current_account
            ).prefetch_related(
                Prefetch('environments'),
                Prefetch('steps', queryset=FlowStep.objects.select_related(
                    'content_type', 'delay', 'group', 'email', 'push'
                    )
                )
            ).select_related('user')

    def get_context_data(self):
        context_data = super().get_context_data()
        context_data.update({
            'highlight': self.kwargs.get('revision', self.object_list.filter(environments=self.current_environment).first().pk)
        })
        return context_data