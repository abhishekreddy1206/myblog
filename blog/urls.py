from blog.views import HomeView, ProjectsView, FindsView, ExperienceView, HobbiesView, ContactView, EducationView
from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
	url(r'^$', HomeView.as_view()),
	url(r'^projects/', ProjectsView.as_view()),
	url(r'^experience/', ExperienceView.as_view()),
	url(r'^finds/', FindsView.as_view()),
	url(r'^hobbies/', HobbiesView.as_view()),
	url(r'^contact/', ContactView.as_view()),
	url(r'^education/', EducationView.as_view()),
]
