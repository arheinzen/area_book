from django.conf.urls import url, patterns, include
from main.views import family_info
from django.views.generic import TemplateView

#HouseholdListView,

urlpatterns = [
	
#	url(r'^household/$', 'main.views.family_info'),
	url(r'^household/$', 'main.views.family_info'),
	url(r'^login/$', TemplateView.as_view(template_name="login.html")),
	url(r'^home/$', TemplateView.as_view(template_name="home.html")),
	url(r'^wardmap/$', TemplateView.as_view(template_name="wardmap.html")),
]