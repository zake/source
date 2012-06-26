from django.contrib import admin

from .models import Article, ArticleBlock


class ArticleBlockInline(admin.StackedInline):
    model = ArticleBlock
    extra = 1
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('', {'fields': (('order', 'title', 'slug'), 'body',)}),
    )

class ArticleAdmin(admin.ModelAdmin):
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('authors', 'people', 'organizations', 'code',)
    list_filter = ('is_live', 'article_type',)
    search_fields = ('title', 'body', 'summary',)
    date_hierarchy = 'pubdate'
    fieldsets = (
        ('', {'fields': (('title', 'slug'), 'subhead', ('pubdate', 'is_live'),)}),
        ('Article relationships', {'fields': ('authors', 'people', 'organizations', 'code',)}),
        ('Article body', {'fields': ('article_type', 'tags', 'summary', 'body',)}),
    )
    inlines = [ArticleBlockInline,]

admin.site.register(Article, ArticleAdmin)