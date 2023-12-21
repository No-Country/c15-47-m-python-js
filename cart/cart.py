from store.models import Book

class Cart():
	def __init__(self, request):
		self.session = request.session

		# get the current session key if it exists
		cart = self.session.get('session_key')

		# if the user is new, no session key. Create one.
		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}

		# make sure cart is available on all pages of site
		self.cart = cart

	def add(self, book, quantity):
		book_id = str(book.id)
		book_qty = str(quantity)
		
		# If a book is already in the cart then just increment quantity by 1
		if book_id in self.cart:
			#self.update(book_id, self.cart[book_id]['quantity'] + 1)
			pass
		else:
			self.cart[book_id] = int(book_qty)
		
		self.session.modified = True

	def cart_total(self):
		# Get books IDS
		book_ids = self.cart.keys()
		# lookup those keys in our books database model
		books = Book.objects.filter(id__in=book_ids)
		# Get quantities
		quantities = self.cart
		# Start counting at 0
		total = 0
		
		for key, value in quantities.items():
			# Convert key string into into so we can do math
			key = int(key)
			for book in books:
				if book.id == key:
					total = total + (book.price * value)

		return total

	def __len__(self):
		return len(self.cart)

	def get_books(self):
		# get ids from cart
		books_ids = self.cart.keys()
		# use ids to lookup books in database model
		books = Book.objects.filter(id__in=books_ids)
		
		# return those looked up books
		return books

	def get_quants(self):
		quantities = self.cart
		return quantities

	def update(self, book, quantity):
		book_id = str(book)
		book_qty = int(quantity)
		
		# get cart
		ourcart = self.cart
		# update dictionary/cart
		ourcart[book_id] = book_qty
		
		self.session.modified = True
		
		thing = self.cart
		return thing

	def delete(self, book):
		book_id = str(book)
		# delete from dictionary/cart
		if book_id in self.cart:
			del self.cart[book_id]
		
		self.session.modified = True

	def clear_cart(self, book):
		# get ids from cart
		books_ids = self.cart.keys()
		# use ids to lookup books in database model
		books = Book.objects.filter(id__in=books_ids)
		# delete from dictionary/cart
		for book in books:
			if book in self.cart:
				del self.cart[book]
		
		self.session.modified = True