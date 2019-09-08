from django.contrib import admin
from .models import Post, Comment, AskQuestion

# we can user decorator as well to reigster the model to admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','body','author','created','updated','status']
    list_filter = ('author','created')
    list_per_page = 20
    search_fields = ['author__username', 'title']
    prepopulated_fields = {'slug':('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')    # we can filter using date

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','content','user','timestamp']

@admin.register(AskQuestion)
class AskQuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'description', 'created', 'status' ]
    list_filter = ('author','created')
    list_per_page = 20
    search_fields = ['author__username', 'title']
    prepopulated_fields = {'slug':('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')

# admin.site.register(Comment, CommentAdmin)
# Register your models here.
# admin.site.register(Post, PostAdmin)