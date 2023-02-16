from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('name','status','parent_cat','child_cat')
    list_filter = ('name',)
    search_fields = ['name', 'description']


admin.site.register(Post,PostAdmin)

