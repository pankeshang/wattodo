from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from todo.views import ItemsView, ItemView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'what_to_do.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'todo.views.index',  name='index'),
    url(r'^items/$', ItemsView.as_view(), name='items' ),
    url(r'^items/add$', 'todo.views.add_item', name='add-item'),
    url(r'^items/(?P<item_id>\d+)$', ItemView.as_view(), name='edit-item'),
    url(r'^items/(?P<item_id>\d+)/delete$', 'todo.views.delete_item', name='delete-item'),
    url(r'^recommend$', 'todo.views.recommend', name='recommend'),
)


from django.conf import settings
print 'settings.DEBUG:', `settings.DEBUG`
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
