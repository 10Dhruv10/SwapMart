from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_displa', views.add_displa, name='add-displa'),
    path('display', views.all_display, name='list-display'),
    path('search/', views.search_results, name='search_results'),
    path('update_displa/<displa_id>', views.update_displa, name="update-displa"),
    path('delete_displa/<displa_id>', views.delete_displa, name='delete-displa'),
    path('access_denied', views.access_denied, name='access_denied'),
    path('contact/', views.contact_view, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)