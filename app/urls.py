from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore
from django.conf import settings as setting  # type: ignore
from django.conf.urls.static import static  # type: ignore
from cars.views import CarDetailView,CarUpdateView,CarDeleteView
from cars.views import  NewCarCreateView, CarsView
from account.views import RegisterView,CustomLoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", RegisterView.as_view(), name="register"),
    path('login/', CustomLoginView.as_view() , name='login'),
    path("", CarsView.as_view(), name="car_views"),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path("new_car/",  NewCarCreateView.as_view(), name="new_car"),
    path("car/<int:pk>/delete/", CarDeleteView.as_view(), name="car_delete"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car_detail"),
] + static(setting.MEDIA_URL, document_root=setting.MEDIA_ROOT)
