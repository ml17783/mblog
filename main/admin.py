from django.contrib import admin
from .models import Blog
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	fieldsets = [
				  ('title',{'fields':['blog_title']}),
				  ('content', {'fields':['blog_content']}),
				  ('published',{'fields':['blog_published']}),
				]

	formfield_overrides = {
	models.TextField: {'widget': TinyMCE()}
	}


admin.site.register(Blog, BlogAdmin)