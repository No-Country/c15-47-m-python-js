from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Book
from django.http import JsonResponse

def cart_summary(request):
	# get the cart
	cart = Cart(request)
	cart_books = cart.get_books
	quantities = cart.get_quants
	context = {
		"cart_books": cart_books,
		"quantities": quantities
	}
	return render(request, "cart_summary.html", context)


def cart_add(request):
	# Get the cart
	cart = Cart(request)
	# test for POST
	if request.POST.get('action') == 'post':
		# Get stuff
		book_id = int(request.POST.get('book_id'))
		book_qty = int(request.POST.get('book_qty'))

		# lookup product in DB
		book = get_object_or_404(Book, id=book_id)

		# Save to session
		cart.add(book=book, quantity=book_qty)
		# Get Cart Quantity
		cart_quantity = cart.__len__()
		# Return response
		response = JsonResponse({'qty': cart_quantity})
		return response

def cart_delete(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# get stuff
		book_id = int(request.POST.get('book_id'))
		# call delete function in Cart
		cart.delete(book=book_id)
		
		response = JsonResponse({'book':book_id})
		return response

def cart_update(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# get stuff
		book_id = int(request.POST.get('book_id'))
		book_qty = int(request.POST.get('book_qty'))
		
		cart.update(book=book_id, quantity=book_qty)
		
		response = JsonResponse({'qty':book_qty})
		return response