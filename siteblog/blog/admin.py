from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

# Register your models here.

from .models import Category, Tag, Post


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'ckeditor'}))

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm
    save_on_top = True
    list_display = ['title', 'slug', 'category', 'created_at', 'get_photo']
    list_filter = ('category',)
    list_editable = ('category',)
    list_display_links = ('title', 'slug')
    search_fields = ('title', 'content')
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'category', 'tags', 'content','photo', 'get_photo', 'views', 'created_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return ''

    get_photo.short_description = 'get_photo'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
