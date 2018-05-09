from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from seguros.tickets import views

urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^$', views.HomePageView, name='home'),
    url(r'^panel$', TemplateView.as_view(template_name='panel.html'), name='panel'),
    url(r'^cobertura$', TemplateView.as_view(template_name='cobertura.html'), name='home'),
    url(r'^dashboard$', TemplateView.as_view(template_name='pages/dashboard.html'), name='dashboard'),
    url(r'^tickets$', TemplateView.as_view(template_name='pages/tickets.html'), name='tickets'),
    url(r'^todos$', TemplateView.as_view(template_name='pages/todos.html'), name='todos'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('seguros.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
