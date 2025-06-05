
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from django.conf import settings as setting # type: ignore
from django.conf.urls.static import static # type: ignore
from cars.views import car_views,car_detail
from cars.views import new_car_view 

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',car_views, name = "car_views" ),
    path('new_car/', new_car_view, name='new_car'),
    path('carro/<int:id>/', car_detail, name='car_detail'),

] + static(setting.MEDIA_URL, document_root=setting.MEDIA_ROOT)