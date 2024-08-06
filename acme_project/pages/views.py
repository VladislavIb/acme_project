"""Pages views."""
from django.views.generic import TemplateView

from birthday.models import Birthday


class HomePage(TemplateView):
    """Home page view."""

    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        """Get context data."""
        context = super().get_context_data(**kwargs)
        context['total_count'] = Birthday.objects.count()
        return context
