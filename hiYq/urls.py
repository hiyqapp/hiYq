from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('account.urls')),
	path('account/', include('account.urls')),
	path('user/', include('user.urls')),
	path('organisation/', include('organisation.urls')),
	path('university/', include('university.urls')),
	path('event/', include('event.urls')),
	path('match/', include('match.urls')),
	path('chat/', include('chat.urls')),
	path('admin/', admin.site.urls),
]
