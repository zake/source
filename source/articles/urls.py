from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

from .views import ArticleList, ArticleDetail


urlpatterns = patterns('',
    # /articles/ is matched as a section in base.urls
    #url(
    #    regex = '^$',
    #    view = ArticleList.as_view(),
    #    kwargs = {},
    #   name = 'article_list',
    #,
    url(
        regex = '^tags/(?P<tag_slug>[-\w]+)/$',
        view = ArticleList.as_view(),
        kwargs = {},
        name = 'article_list_by_tag',
    ),
    url(
        regex = '^tags/$',
        view = redirect_to,
        kwargs  = {'url': '/articles/'},
        name = 'article_list_tags',
    ),
    url(
        regex = '^(?P<slug>[-\w]+)/$',
        view = ArticleDetail.as_view(),
        kwargs = {},
        name = 'article_detail',
    ),
)
