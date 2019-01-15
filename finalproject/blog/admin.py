from django.contrib import admin
from .models import Posts,Profile
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author']
    search_fields = ['title','author']
    list_filter = ['title','author','created']

class  ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','photo','dob']

admin.site.register(Posts,PostAdmin)
admin.site.register(Profile, ProfileAdmin)



