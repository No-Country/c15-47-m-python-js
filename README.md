# Bookstore Project
This is an online bookstore built using Python and Django framework. The project enables users to register, log in, and purchase books from the available library.

## Features
* **User Authentication:** Users can create accounts, log in, and log out securely.
* **Book Catalog:** Browse a wide range of books available in the online library.
* **Shopping Cart:** Users can add books to their cart for purchasing.
* **Checkout Process:** Smooth and secure payment process to buy selected books.
* **Admin Panel:** Manage books, users, and orders efficiently through the admin interface.

## Technologies Used
* **Python:** Backend development using Python language.
* **Django:** Web framework for rapid development and clean design.
* **Bootstrap:** Frontend design and layout for a responsive and visually appealing interface.
* **HTML/CSS:** Structure and styling of web pages.

## Getting Started
### Prerequisites
* Python installed on your machine.
* Django framework installed `pip install django`.

### Installation
+ Clone the repository: `git clone https://github.com/yourusername/bookstore.git`
+ Navigate to the project directory.
+ Create a virtual environment: `python -m venv env`
+ Activate the virtual environment:
  * On Windows: `env\Scripts\activate`
  * On macOS and Linux: `source env/bin/activate`
+ Install dependencies: `pip install -r requirements.txt`
+ Run migrations: `python manage.py migrate`
+ Create a superuser (admin): `python manage.py createsuperuser`
+ Start the server: `python manage.py runserver`
+ 

### Usage
* Access the admin panel by going to `http://localhost:8000/admin/` and log in using the superuser credentials created earlier.
* Add books to the library using the admin interface.
* Users can register and log in to their accounts.
* Browse the book catalog, add books to the cart, and proceed to checkout to purchase.

### Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for any improvements or new features.

### License
This project is licensed under the MIT License.
