# BookStop-Marketplace

BookStop-Marketplace is a Django-based web application designed to facilitate buying and selling of books within a campus environment. This platform aims to provide a convenient marketplace for both seniors and juniors to exchange books, helping students save money and fostering a sense of community within the campus.

## Features

- **User Authentication**: Users can create accounts, log in, and log out securely.
- **Book Listings**: Users can list books they want to sell, specifying details such as title, author, condition, and price.
- **Book Details**: Detailed information about each book listing, including images, description, and seller information.
- **User Profiles**: Each user has a profile page where they can manage their listings, view messages, and update their information.
- **Admin Panel**: Admins have access to a powerful admin panel to manage users, listings, and reported content.
- **Responsive Design**: The website is designed to be mobile-friendly, ensuring a seamless experience across devices.

## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/BookStop-Marketplace.git
```

2. Navigate to the project directory:
```
cd BookStop-Marketplace
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Apply migrations:
```
python manage.py migrate
```

5. Create a superuser (admin account):
```
python manage.py createsuperuser
```

6. Start the development server:
```
python manage.py runserver
```


7. Access the application at `http://localhost:8000` in your web browser.

## Usage

- **User Registration**: Users can register for an account by providing basic information.
- **Listing Books**: Logged-in users can list books they want to sell by providing details and uploading images.
- **Managing Listings**: Users can edit or delete their listings from their profile page.
- **Admin Control**: Admins can manage users, listings, and reported content through the admin panel.

## Contributing

Contributions are welcome! If you'd like to contribute to BookStop-Marketplace, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.

## Acknowledgements

- This project was inspired by the need for a convenient and efficient way for students to buy and sell books within a campus environment.
- Special thanks to the Django community for their invaluable resources and documentation.
