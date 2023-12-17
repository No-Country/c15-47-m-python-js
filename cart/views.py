from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Book
from django.http import JsonResponse

def cart_summary(request):
    return render(request, "cart_summary.html", {})






def cart_add(request):
	# Get the cart
	cart = Cart(request)
	# test for POST
	if request.POST.get('action') == 'post':
		# Get stuff
		book_id = int(request.POST.get('book_id'))

		# lookup product in DB
		book = get_object_or_404(Book, id=book_id)
		
		# Save to session
		cart.add(book=book)

		# Get Cart Quantity
		cart_quantity = cart.__len__()

		# Return resonse
		# response = JsonResponse({'Product Name: ': product.name})
		response = JsonResponse({'qty': cart_quantity})
		return response

def cart_delete(request):
    pass

def cart_update(request):
    pass