from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.contrib import messages

from .models import Item, OrderItem, Order

# Create your views here.
def home(request):
	return render(request, 'summer/home.html')

def points(request):
	return render(request, 'summer/points.html')

def products(request):
	context = {
		'items': Item.objects.all()
	}
	return render(request, "summer/product.html", context)

def checkout(request):
	return render(request, "summer/checkout.html")

class StoreView(ListView):
	model = Item
	template_name = "summer/store.html"

class ItemDetailView(DetailView):
	model = Item
	template_name = "summer/product.html"

def add_to_cart(request, slug):
	item = get_object_or_404(Item, slug=slug)
	order_item, created = OrderItem.objects.get_or_create(item=item,
												 user=request.user,
												 ordered=False)
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
		order = order_qs[0]
		# check if the order item is in the order
		if order.items.filter(item__slug=item.slug).exists():
			order_item.quantity += 1
			order_item.save()
			messages.info(request, "Quantity updated!")
		else:
			order.items.add(order_item)
			messages.info(request, "Added to cart!")
			return redirect("summer:product", slug=slug)
	else:
		ordered_date = timezone.now()
		order = Order.objects.create(user=request.user, ordered_date=ordered_date)
		order.items.add(order_item)
		messages.info(request, "Successfully added to cart!")
		return redirect("summer:product", slug=slug)

def remove_from_cart(request, slug):
	item = get_object_or_404(Item, slug=slug)
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
		order = order_qs[0]
		# check if the order item is in the order
		if order.items.filter(item__slug=item.slug).exists():
			order_item = OrderItem.objects.filter(item=item,
												 user=request.user,
												 ordered=False)[0]
			order.items.remove(order_item)
			messages.info(request, "Removed from cart.")
			return redirect("summer:product", slug=slug)
		else:
			messages.info(request, "Nothing is in cart.")
			return redirect("summer:product", slug=slug)
	else:
		messages.info(request, "No order taken yet.")
		return redirect("summer:product", slug=slug)


# keep for now
# def old_store(request):
# 	products = Product.objects.all()
# 	return render(request, 'summer/store.html', {
# 		'products': products
# 		})
#
# def store_all(request):
# 	return render(request, 'summer/store-all.html')
#
# def store_bibles(request):
# 	return render(request, 'summer/store-bibles.html')
#
# def store_bracelets(request):
# 	return render(request, 'summer/store-bracelets.html')
#
# def store_candies(request):
# 	return render(request, 'summer/store-candies.html')

# def imhere(request):
# 	return render(request, 'summer/imhere.html')
