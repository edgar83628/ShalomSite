from django.urls import path
from . import views
from .views import (
	StoreView,
	ItemDetailView,
)

app_name = 'summer'

urlpatterns = [
	path("home", views.home, name="home"),
	path("points", views.points, name="points"),
	path("store", StoreView.as_view(), name="store"),
	path('product/<str:slug>/', ItemDetailView.as_view(), name='product'),
	path("checkout", views.checkout, name="checkout"),
	path('add-to-cart/<str:slug>/', views.add_to_cart, name='add-to-cart'),
	path('remove-from-cart/<str:slug>/', views.remove_from_cart, name='remove-from-cart'),

]

	# path("old_store", views.old_store, name="old_store"),
	# path("store_all", views.store_all, name="store_all"),
	# path("store_bibles", views.store_bibles, name="store_bibles"),
	# path("store_bracelets", views.store_bracelets, name="store_bracelets"),
	# path("store_candies", views.store_candies, name="store_candies"),

	# path("checkedin", views.checkedin, name="checkedin"),
	# path("logout", views.logout, name="logout"),
	# path("checkin", views.checkin, name="checkin"),
	# path("imhere", views.imhere, name="imhere"),