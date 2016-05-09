from django.db import models

class Collection(models.Model):
	name = models.CharField(max_length=50)
	date = models.DateField()
	location = models.CharField(max_length=50)
	description = models.TextField(max_length=140)
	active = models.BooleanField(default=True)
	def __str__(self):
		return "%d: %s" % (self.pk, self.name)

class CollectionPhoto(models.Model):
	collection = models.ForeignKey('Collection', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='./main/dbapi/static/photos/collections')
	title = models.CharField(max_length=50)
	caption = models.TextField(max_length=140)
	active = models.BooleanField(default=True)

class Category(models.Model):
	name = models.CharField(max_length=25)
	active = models.BooleanField(default=True)
	def __str__(self):
		return "%d: %s" % (self.pk, self.name)

class Project(models.Model):
	title = models.CharField(max_length=50)
	category = models.ForeignKey('Category')
	date = models.DateField()
	description = models.TextField(max_length=500)
	active = models.BooleanField(default=True)
	def __str__(self):
		return "%d: %s" % (self.pk, self.title)
	
class ProjectPhoto(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='./main/dbapi/static/photos/projects')
	caption = models.CharField(max_length=140)
	active = models.BooleanField(default=True)

class Team(models.Model):
	name = models.CharField(max_length=50)
	role = models.CharField(max_length=75)
	description = models.TextField(max_length=500)
	active = models.BooleanField(default=True)
	def __str__(self):
		return "%d: %s" % (self.pk, self.name)
	
class TeamPhoto(models.Model):
	team = models.ForeignKey('Team', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='./main/dbapi/static/photos/teams')
	caption = models.CharField(max_length=140)
	active = models.BooleanField(default=True)

class Post(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateField()
	body = models.TextField(max_length=500)
	active = models.BooleanField(default=True)
	def __str__(self):
		return "%d: %s" % (self.pk, self.title)
	
class PostPhoto(models.Model):
	post = models.ForeignKey('Post', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='./main/dbapi/static/photos/posts')
	caption = models.CharField(max_length=140)
	active = models.BooleanField(default=True)