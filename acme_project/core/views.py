"""Core views."""
from django.shortcuts import render


def page_not_found(request, exception):
    """Page not found."""
    return render(request, 'core/404.html', status=404)


def csrf_failure(request, reason=''):
    """CSRF failure."""
    return render(request, 'core/403csrf.html', status=403)