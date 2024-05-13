from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Categorys(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Sizes(models.Model):
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.size
class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    sizes = models.ManyToManyField(Sizes)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    main_image = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name + " Image"

class Orders(models.Model):
    '''
    Модель для покупки
    '''

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    )

    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name}"


class Banners(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='banners/', null=True, blank=True)
    active = models.BooleanField()
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title


class Comments(models.Model):
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='запись')

    text = models.TextField(verbose_name='Текст комментария', help_text='Введите текст комментария')

    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата публикации', )
    rate = models.PositiveIntegerField(default=1)