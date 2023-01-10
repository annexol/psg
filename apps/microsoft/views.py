from django.db.models import Q
from django.views.generic import ListView
from .models import Apps


class MicrosoftApps(ListView):
    model = Apps
    template_name = 'microsoft/apps.html'
    context_object_name = 'apps'
    extra_context = {'title': 'Microsoft Apps'}

    def get_ordering(self):

        """
        Getting ordering apps
        :return:
        """

        self.ordering = self.request.GET.get('orderby')
        if self.ordering:
            self.extra_context = {'orderby': self.ordering, 'paginate_by': self.paginate_by}
        else:
            self.ordering = 'id'
        return self.ordering

    def get_paginate_by(self, queryset):

        """
        Getting pagination
        :param queryset:
        :return:
        """

        if self.request.GET.get('paginateby'):
            self.paginate_by = self.request.GET.get('paginateby')
        else:
            self.paginate_by = 10
        self.extra_context = {'paginate_by': self.paginate_by, 'orderby': self.ordering}

        return self.paginate_by


class FilterMicrosoftApps(ListView):
    model = Apps
    template_name = 'microsoft/filter_apps.html'
    context_object_name = 'filter_apps'
    extra_context = {'title': 'Filter Microsoft Apps'}

    def get_queryset(self):

        """
        Getting filtered apps
        :return:
        """

        query = self.request.GET.get('usertext')
        if query:
            lookups = Q(name__icontains=query)
            self.queryset = Apps.objects.filter(lookups).distinct()
        return self.queryset

