from django.urls import path
from . import views

from .views import successView

urlpatterns = [
	path("", views.project_index, name="project_index"),
	path("<int:pk>/", views.project_detail, name="project_detail"),
    path("success/", successView, name="success"),
	]