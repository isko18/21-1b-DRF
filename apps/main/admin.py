from django.contrib import admin
from apps.main.models import Settings, Products, ProductImage
from django.utils.html import format_html
# Register your models here.

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ['image_tag']
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="50px" />'.format(obj.image.url))
    
    image_tag.short_description = "Изображение"
    
    
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display=('title', 'description', 'price', 'is_active', 'image_tag')
    list_editable=['is_active']
    readonly_fields = ('created_at',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {'fields': (
            'title',
            'slug',
            'description',
            'price',
            'is_active',
            'created_at',
        )}),
    )
    
    inlines = [ProductImageAdmin]
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="30px" />'.format(obj.get_first_image()))
    
    image_tag.short_description = "Изображение"