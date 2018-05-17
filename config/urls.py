from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from seguros.tickets import views

from django.urls import path


urlpatterns = [
    #url(r'^$', views.HomePageView, name='home'),
    path(r'', views.HomePageView.as_view(), name='home'),
    path(r'cotizador/years/<int:brand_id>/', views.get_years, name='years-brand'),
    path(r'cotizador/models/<int:brand_id>/<int:year>/', views.get_models, name='models-brand'),
    path(r'cotizador/versions/<int:brand_id>/<int:year>/<int:model_id>/', views.get_versions, name='versions-brand'),
    

    #url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^cobertura$', TemplateView.as_view(template_name='cobertura.html'), name='home'),
    url(r'^dashboard$', TemplateView.as_view(template_name='pages/dashboard.html'), name='dashboard'),
    url(r'^tickets$', TemplateView.as_view(template_name='pages/tickets.html'), name='tickets'),
    url(r'^todos$', TemplateView.as_view(template_name='pages/todos.html'), name='todos'),
    url(r'^tareas$', TemplateView.as_view(template_name='pages/tareas.html'), name='tareas'),

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
