from django.views.generic import TemplateView


class BaseLayoutView(TemplateView):
    template_name = "base_layout.html"
