from django.shortcuts import redirect, render
from cart.cart import Cart
from payment.forms import ShippingForm , PaymentForm
from payment.models import ShippingAddress
from django.contrib import messages

def payment_success(request):
	return render(request, "payment/checkout.html", {})


def checkout(request):
	
	# Get the cart
	cart = Cart(request)
	cart_products = cart.get_prods
	quantities = cart.get_quants
	totals = cart.cart_total()
	#return render(request, "payment/checkout.html", {"cart_products":cart_products, "quantities":quantities,"totals":totals})
	if request.user.is_authenticated:
		# Checkout as logged in user
		# Shipping User
		shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
		# Shipping Form
		shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
		return render(request, "payment/checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form })
	else:
		# Checkout as guest
		shipping_form = ShippingForm(request.POST or None)
		return render(request, "payment/checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})
	

def billing_info(request):
	if request.POST:
		# Get the cart
		cart = Cart(request)
		cart_products = cart.get_prods
		quantities = cart.get_quants
		totals = cart.cart_total()
		#shipping_form = request.POST this is just taking the previous form and sending it to next page
		#check if the user is logged in
		if request.user.is_authenticated :
			#Get the billing form 
			billing_form = PaymentForm()
			return render(request, "payment/billing_info.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form})
		else :
			#not logged in
			#Get the billing form 
			billing_form = PaymentForm()
			return render(request, "payment/billing_info.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form})
	else:
		messages.success(request, "Access Denied")
		return redirect('home')
	
