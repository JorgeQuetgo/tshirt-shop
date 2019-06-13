from django.conf.urls import url
from shop import views

departament_list =views.DepartamentViewSet.as_view({
    'get': 'list',
})

urlpatterns = [
    # list of departaments
    url(r'^tshirtshop/departaments$', departament_list, name='departament-list'),
]