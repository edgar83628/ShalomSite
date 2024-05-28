from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

# Create your models here.


# HOW TO BUILD AN E-COMMERCE WEBSITE WITH DJANGO AND PYTHON

CATEGORY_CHOICES = (
	('C', 'Candies'),
	('B', 'Bibles'),
	('BC', 'Bracelets')
)

LABEL_CHOICES = (
	('P', 'primary'),
	('S', 'secondary'),
	('D', 'danger')
)

class Item(models.Model):
	title = models.CharField(max_length=100)
	price = models.IntegerField()
	discount_price = models.IntegerField(blank=True, null=True)
	category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
	label = models.CharField(choices=LABEL_CHOICES, max_length=1)
	slug = models.SlugField()
	description = models.TextField(blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("summer:product", kwargs={
			'slug': self.slug
		})

	def get_add_to_cart_url(self):
		return reverse("summer:add-to-cart", kwargs={
			'slug': self.slug
		})

	def get_remove_from_cart_url(self):
		return reverse("summer:remove-from-cart", kwargs={
			'slug': self.slug
		})


class OrderItem(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	ordered = models.BooleanField(default=False)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return f"{self.quantity} of {self.item.title}"

class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	items = models.ManyToManyField(OrderItem)
	start_date = models.DateTimeField(auto_now_add=True)
	ordered_date = models.DateTimeField()
	ordered = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username

# class UserPoints(AbstractUser):
# 	points = models.PositiveIntegerField(default=5, verbose_name='points')
#
# 	def modify_points(self, added_points):
# 		self.points += added_points
# 		self.save()
#







# FIRST TRY MIGHT DELETE LATER

# class Category(models.Model):
# 										#db_index research needed
# 	name = models.CharField(max_length=225, db_index=True)
# 	slug = models.SlugField(max_length=225, unique=True)
#
# 	class Meta:
# 		verbose_name_plural = 'categories'
#
# 	def __str__(self):
# 		return self.name
#
# class Product(models.Model):
# 																#on_delete & CASCADE research needed
# 	#category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
# 	created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
# 	title = models.CharField(max_length=225)
# 	#author might change, to brand
# 	author = models.CharField(max_length=225, default='admin')
# 	#description = models.TextField(blank=True)
# 	image = models.ImageField(upload_to='images/')
# 	slug = models.SlugField(max_length=225)
# 	price = models.DecimalField(max_digits=4, decimal_places=2)
# 	in_stock = models.BooleanField(default=True)
# 	is_active = models.BooleanField(default=True)
# 	created = models.DateTimeField(auto_now_add=True)
# 	updated = models.DateTimeField(auto_now=True)
#
# 	class Meta:
# 		verbose_name_plural = 'products'
# 		ordering = ('-created',)
#
# 	def __str__(self):
# 		return self.title
#
#



