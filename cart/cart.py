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

    def add(self, book):
        book_id = str(book.id)
        # If a book is already in the cart then just increment quantity by 1
        if book_id in self.cart:
            #self.update(book_id, self.cart[book_id]['quantity'] + 1)
            pass
        else:
            self.cart[book_id] = {'price: ': str(book.price)}
        
        self.session.modified = True

    def __len__(self):
        return len(self.cart)