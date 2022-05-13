from django.contrib import admin
# Register your models here.
from app.models import Category,Contact,Post


admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Post)
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = (,)
# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = (,)
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = (,)
#     readonly_fields = ('slug',)