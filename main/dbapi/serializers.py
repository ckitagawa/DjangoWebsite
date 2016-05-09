from .models import Collection, CollectionPhoto 
from .models import Project, ProjectPhoto, Category
from .models import Team, TeamPhoto
from .models import Post, PostPhoto
from django.contrib.auth.models import User #, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('pk', 'username', 'email')

class CollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Collection
		fields = ('pk', 'name', 'date', 'location', 'description', 'active')

class CollectionPhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model = CollectionPhoto
		fields = ('pk', 'collection', 'image', 'title', 'caption', 'active')

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('pk', 'name', 'active')

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = ('pk', 'title', 'category', 'date', 'description', 'active')

class ProjectPhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProjectPhoto
		fields = ('pk', 'project', 'image', 'caption', 'active')

class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Team
		fields = ('pk', 'name', 'role', 'description', 'active')

class TeamPhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model = TeamPhoto
		fields = ('pk', 'team', 'image', 'caption', 'active')

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('pk', 'title', 'date', 'body', 'active')

class PostPhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model = PostPhoto
		fields = ('pk', 'post', 'image', 'caption', 'active')