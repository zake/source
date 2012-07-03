from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Code
from taggit.models import Tag


class CodeList(ListView):
    model = Code
    
    def dispatch(self, *args, **kwargs):
        self.tag_slug = kwargs.get('tag_slug', None)
        self.tag = None

        if self.tag_slug:
            self.tag = get_object_or_404(Tag, slug=self.tag_slug)

        return super(CodeList, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = Code.live_objects.prefetch_related('organizations')

        if self.tag_slug:
            queryset = queryset.filter(tags__slug=self.kwargs['tag_slug'])

        return queryset

    def get_context_data(self, **kwargs):
        context = super(CodeList, self).get_context_data(**kwargs)
        context['active_nav'] = 'Code'
        context['tag'] = self.tag

        return context


class CodeDetail(DetailView):
    model = Code

    def get_queryset(self):
        queryset = Code.live_objects.prefetch_related('codelink_set', 'people', 'organizations', 'article_set')
        
        return queryset
