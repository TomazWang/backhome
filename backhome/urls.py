from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'backhome.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'page.views.select_page'),
    url(r'^ajax/decision', 'page.ajax.make_decision'),
    # url(r'^ajax/select_member', 'page.dao.select_member'),
    url(r'^see_all$','page.views.see_all'),
    url(r'^clear_cookie','page.ajax.clear_cookie')
)
