from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from apps.utils import get_product_upload_path
from slugify import slugify
import uuid
# Create your models here.

class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"
        
        
class Products(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Тут должен быть название товара"
    )
    slug = models.TextField(
        verbose_name="SLUG",
        unique=True, null=True
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Тут должен быть описание товара"
    )
    price = models.DecimalField(
        max_digits=100,
        decimal_places=2,
        verbose_name="Цена"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        null=True
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активный ?"
    )
    
    def __str__(self):
        return self.title
    
    def get_first_image(self) -> 'ProductImage':
        product_image = ProductImage.objects.filter(product=self).first()
        return product_image.image.url if product_image else None
    def save(self, *args, **kwargs):
        # Генерация slug, если он отсутствует
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = base_slug
            # Уникализация slug
            while Products.objects.filter(slug=self.slug).exists():
                unique_suffix = uuid.uuid4().hex[:6]
                self.slug = f"{base_slug}-{unique_suffix}"
        # Вызов метода save родительского класса
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        
class ProductImage(models.Model):
    product = models.ForeignKey(
        to="Products",
        on_delete=models.CASCADE,
        verbose_name="Товар",
        related_name="product_image"
    )
    image = ProcessedImageField(
        upload_to=get_product_upload_path,
        verbose_name="Изображение",
        processors=[ResizeToFill(100,50)],
        format='webp',
        options={'quality': 100}
    )
    position = models.PositiveIntegerField(
        default=0,
        blank=True, null=True
    )
    
    def __str__(self):
        return str(self.image.name)
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['position',]