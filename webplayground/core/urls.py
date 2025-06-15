from django.urls import path
from .views import HomeView, AboutView, ProjectsView, ContactView, SampleView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('sample/', SampleView.as_view(), name='sample'),

]
