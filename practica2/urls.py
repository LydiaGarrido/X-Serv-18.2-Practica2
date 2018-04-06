from django.conf.urls import include, url
from django.contrib import admin
from acorta import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'practica2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.barra, name="Pagina principal"),
    url(r'^(\d+)', views.redirect, name="Redireccion al recurso"),
    url(r'^.+', views.error, name="Error")
]
