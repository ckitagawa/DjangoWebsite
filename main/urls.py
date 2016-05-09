from django.conf.urls import include, url, patterns
from rest_framework_nested import routers
from main.dbapi import views

#Users
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

#Collections
collections_base_router = routers.DefaultRouter()
collections_base_router.register(r'collections', views.CollectionViewSet, base_name='collections')

collections_router = routers.NestedSimpleRouter(collections_base_router, r'collections', lookup='collection')
collections_router.register(r'photos', views.CollectionPhotoViewSet, base_name='photos')

#Projects
projects_base_router = routers.DefaultRouter()
projects_base_router.register(r'categories', views.CategoryViewSet, base_name='categories')

projects_router = routers.NestedSimpleRouter(projects_base_router, r'categories', lookup='category')
projects_router.register(r'projects', views.ProjectViewSet, base_name='project')

project_photos_router = routers.NestedSimpleRouter(projects_router, r'projects', lookup='project')
project_photos_router.register(r'photos', views.ProjectPhotoViewSet, base_name='photos')

#Teams

teams_base_router = routers.DefaultRouter()
teams_base_router.register(r'teams', views.TeamViewSet, base_name='teams')

teams_router = routers.NestedSimpleRouter(teams_base_router, r'teams', lookup='team')
teams_router.register(r'photos', views.TeamPhotoViewSet, base_name='photos')

#Posts

posts_base_router = routers.DefaultRouter()
posts_base_router.register(r'posts', views.PostViewSet, base_name='posts')

posts_router = routers.NestedSimpleRouter(posts_base_router, r'posts', lookup='post')
posts_router.register(r'photos', views.PostPhotoViewSet, base_name='photos')

urlpatterns = [
	url(r'^api/$', views.api_root),
	url(r'^api/', include(router.urls)),
	url(r'^api/', include(collections_base_router.urls)),
	url(r'^api/', include(collections_router.urls)),
	url(r'^api/', include(projects_base_router.urls)),
	url(r'^api/', include(projects_router.urls)),
	url(r'^api/', include(project_photos_router.urls)),
	url(r'^api/', include(teams_base_router.urls)),
	url(r'^api/', include(teams_router.urls)),
	url(r'^api/', include(posts_base_router.urls)),
	url(r'^api/', include(posts_router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^$', views.index, name='index')
]
