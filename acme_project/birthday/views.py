"""Birthday views."""
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .forms import BirthdayForm, CongratulationForm
from .models import Birthday
from .utils import calculate_birthday_countdown


@login_required
def add_comment(request, pk):
    """Add comment."""
    birthday = get_object_or_404(Birthday, pk=pk)
    form = CongratulationForm(request.POST)
    if form.is_valid():
        congratulation = form.save(commit=False)
        congratulation.author = request.user
        congratulation.birthday = birthday
        congratulation.save()
    return redirect('birthday:detail', pk=pk)


class OnlyAuthourMixin(UserPassesTestMixin):
    """Only authour mixin."""

    def test_func(self):
        """Test func."""
        object = self.get_object()
        return object.author == self.request.user


class BirthdayListView(ListView):
    """Birthday list view."""

    model = Birthday
    queryset = Birthday.objects.prefetch_related(
        'tags'
    ).select_related('author')
    ordering = 'id'
    paginate_by = 10


class BirthdayCreateView(LoginRequiredMixin, CreateView):
    """Birthday create view."""

    model = Birthday
    form_class = BirthdayForm

    def form_valid(self, form):
        """Form valid."""
        form.instance.author = self.request.user
        return super().form_valid(form)


class BirthdayUpdateView(LoginRequiredMixin, OnlyAuthourMixin, UpdateView):
    """Birthday update view."""

    model = Birthday
    form_class = BirthdayForm


class BirthdayDeleteView(LoginRequiredMixin, OnlyAuthourMixin, DeleteView):
    """Birthday delete view."""

    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayDetailView(DetailView):
    """Birthday detail view."""

    model = Birthday

    def get_context_data(self, **kwargs):
        """Get context data."""
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        context['form'] = CongratulationForm()
        context['congratulations'] = (
            self.object.congratulations.select_related('author')
        )
        return context
