from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class DashboardView(TemplateView):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        access = self.request.user.is_superuser or self.request.user.is_staff
        if not access:
            return redirect(reverse_lazy('dashboard'))
        return super(DashboardView, self).dispatch(request, *args, **kwargs)
    template_name = 'dashboard/dashboard.html'
