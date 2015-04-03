from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'backhome.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    # pages
    url(r'^$', 'page.views.select_page'),
    url(r'^see_all$','page.views.see_all'),

    # func
    url(r'^ajax/login','page.ajax.login'),
    url(r'^clear_cookie','page.ajax.clear_cookie'),

    # sign in
    url(r'^signin', 'page.views.signin'),

    # db select
    url(r'^ajax/search_member','page.ajax.search_member'),
    url(r'^ajax/get_all_group','page.ajax.get_all_group'),

    # db create
    url(r'^ajax/decision', 'page.ajax.make_decision'),
    url(r'^ajax/new_member','page.ajax.new_member'),
    url(r'^ajax/new_group','page.ajax.new_group'),
)
