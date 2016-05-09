from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.decorators import api_view
from main.dbapi.serializers import UserSerializer 
from main.dbapi.serializers import CollectionSerializer, CollectionPhotoSerializer
from main.dbapi.serializers import ProjectSerializer, ProjectPhotoSerializer, CategorySerializer
from main.dbapi.serializers import PostSerializer, PostPhotoSerializer
from main.dbapi.serializers import TeamSerializer, TeamPhotoSerializer
from django.contrib.auth.models import User 
from .models import Collection, CollectionPhoto 
from .models import Project, ProjectPhoto, Category
from .models import Post, PostPhoto
from .models import Team, TeamPhoto
from django.http import HttpResponse
from django.template import loader

def index(request):
	template = loader.get_template('index.html')
	context = {}
	return HttpResponse(template.render(context, request)) 

@api_view(['GET'])
def api_root(request, format=None):
	return Response({
    	'users': reverse('user-list', request=request, format=format),
        'collections': reverse(r'collections-list', request=request, format=format),
        'categories': reverse(r'categories-list', request=request, format=format),
        'teams': reverse(r'teams-list', request=request, format=format),
        'posts': reverse(r'posts-list', request=request, format=format),
	})

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	model = User
	serializer_class = UserSerializer

class CollectionViewSet(viewsets.ModelViewSet):
	serializer_class = CollectionSerializer
	queryset = Collection.objects.all()

class CollectionPhotoViewSet(mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
	serializer_class = CollectionPhotoSerializer
	queryset = CollectionPhoto.objects.all()

	def list(self, request, collection_pk=None):
		queryset = CollectionPhoto.objects.filter(collection=collection_pk)
		serializer = CollectionPhotoSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None, collection_pk=None):
		queryset = CollectionPhoto.objects.filter(pk=pk, collection=collection_pk)
		photos = get_object_or_404(queryset, pk=pk)
		serializer = CollectionPhotoSerializer(photos)
		return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class ProjectViewSet(mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer

	def list(self, request, category_pk=None):
		queryset = Project.objects.filter(category=category_pk)
		serializer = ProjectSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None, category_pk=None):
		queryset = Project.objects.filter(pk=pk, category=category_pk)
		projects = get_object_or_404(queryset, pk=pk)
		serializer = ProjectSerializer(projects)
		return Response(serializer.data)

class ProjectPhotoViewSet(mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
	queryset = ProjectPhoto.objects.all()
	serializer_class = ProjectPhotoSerializer

	def list(self, request, project_pk=None, category_pk=None):
		queryset = ProjectPhoto.objects.filter(project=project_pk)
		serializer = ProjectPhotoSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None, project_pk=None, category_pk=None):
		queryset = ProjectPhoto.objects.filter(pk=pk, project=project_pk)
		photos = get_object_or_404(queryset, pk=pk)
		serializer = ProjectPhotoSerializer(photos)
		return Response(serializer.data)

class TeamViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer

class TeamPhotoViewSet(mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
	queryset = TeamPhoto.objects.all()
	serializer_class = TeamPhotoSerializer

	def list(self, request, team_pk=None):
		queryset = TeamPhoto.objects.filter(team=team_pk)
		serializer = TeamPhotoSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None, team_pk=None):
		queryset = TeamPhoto.objects.filter(pk=pk, team=team_pk)
		photos = get_object_or_404(queryset, pk=pk)
		serializer = TeamPhotoSerializer(photos)
		return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all().order_by('-date')
	serializer_class = PostSerializer

class PostPhotoViewSet(mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
	queryset = PostPhoto.objects.all()
	serializer_class = PostPhotoSerializer

	def list(self, request, post_pk=None):
		queryset = PostPhoto.objects.filter(post=post_pk)
		serializer = PostPhotoSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None, post_pk=None):
		queryset = PostPhoto.objects.filter(pk=pk, post=post_pk)
		photos = get_object_or_404(queryset, pk=pk)
		serializer = PostPhotoSerializer(photos)
		return Response(serializer.data)