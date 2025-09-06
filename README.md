# 🛒 BuyItMe - E-commerce Platform

![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![Django](https://img.shields.io/badge/django-v5.1.4-green.svg)
![Vue.js](https://img.shields.io/badge/vue.js-v3.5.13-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A complete e-commerce platform built with **Django REST Framework** and **Vue.js**, featuring shopping cart, wishlists, JWT authentication, and comprehensive order management.

## 🌟 Features

### 🔐 Authentication & User Management
- **JWT Authentication** with automatic token refresh
- **User Registration & Login** with email verification
- **Password Reset** functionality with secure codes
- **Google OAuth2** integration ready
- **User Profile** management with update capabilities

### 🛍️ E-commerce Core Features
- **Product Catalog** with categories and search
- **Shopping Cart** with guest and authenticated user support
- **Order Management** with multiple status tracking
- **Wishlist System** with public sharing capabilities
- **Favorite Wishlists** to bookmark others' lists

### 🎨 Frontend Features
- **Vue 3** with Composition API (`<script setup>`)
- **Pinia** for state management
- **Vue Router** with authentication guards
- **Responsive Design** with clean UI
- **Real-time** cart and wishlist updates

### ⚙️ Technical Features
- **REST API** with 43+ endpoints
- **Django Admin** interface with custom configurations
- **File Upload** support with django-attachments
- **Fake Data Generator** for development
- **CORS** configured for frontend-backend communication
- **Modular Architecture** for easy maintenance

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- npm or yarn

### 🖥️ Backend Setup (Django)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd buyitme_project
   ```

2. **Create virtual environment**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment configuration**
   ```bash
   # Create .env file in backend directory
   echo "SECRET_KEY=your-secret-key-here" > .env
   echo "DEBUG=True" >> .env
   echo "ALLOWED_HOSTS=localhost,127.0.0.1" >> .env
   ```

5. **Database setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Generate fake data (optional)**
   ```bash
   python manage.py create_fake_data
   ```

8. **Start development server**
   ```bash
   python manage.py runserver
   ```

   🎉 Backend will be available at: `http://localhost:8000`
   📊 Admin panel: `http://localhost:8000/admin`
   📖 API Documentation: `http://localhost:8000/api/`

### 🎨 Frontend Setup (Vue.js)

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

   🎉 Frontend will be available at: `http://localhost:5173`

## 📁 Project Structure

```
buyitme_project/
├── backend/                     # Django REST API
│   ├── buyitme_project/         # Main project settings
│   │   ├── settings.py          # Django configuration
│   │   ├── urls.py              # Main URL routing
│   │   └── wsgi.py              # WSGI configuration
│   ├── buyitme_app/             # Main application
│   │   ├── models/              # Database models
│   │   │   ├── user.py          # User & PasswordCode models
│   │   │   ├── product.py       # Product model with gallery
│   │   │   ├── cart.py          # Cart & CartItem models
│   │   │   ├── order.py         # Order & OrderItem models
│   │   │   └── wishlist.py      # Wishlist models
│   │   ├── serializers/         # DRF serializers
│   │   ├── views/               # API views with @api_view
│   │   ├── urls/                # URL routing by module
│   │   ├── admin.py             # Django admin configuration
│   │   └── management/commands/ # Custom management commands
│   └── requirements.txt         # Python dependencies
├── frontend/                    # Vue.js application
│   ├── src/
│   │   ├── views/               # Vue components (pages)
│   │   ├── stores/              # Pinia state management
│   │   │   └── modules/         # Store modules (auth, cart, etc.)
│   │   ├── services/            # HTTP service layer
│   │   ├── composables/         # Vue composables
│   │   ├── utils/               # Utility functions
│   │   ├── router/              # Vue Router configuration
│   │   └── App.vue              # Root component
│   ├── package.json             # Node.js dependencies
│   └── vite.config.js           # Vite configuration
└── README.md                    # This file
```

## 📡 API Endpoints

### 🔐 Authentication
- `POST /api/auth/signup/` - User registration
- `POST /api/auth/signin/` - User login
- `POST /api/auth/logout/` - User logout
- `GET /api/auth/profile/` - Get user profile
- `POST /api/auth/profile/update/` - Update profile
- `POST /api/auth/password/change/` - Change password
- `POST /api/auth/password/reset/send/` - Send reset code
- `POST /api/auth/password/reset/verify/` - Verify reset code

### 🛍️ Products
- `GET /api/products/` - List products
- `GET /api/products/{id}/` - Product detail
- `GET /api/products/category/` - Products by category
- `GET /api/products/search/` - Search products
- `GET /api/products/categories/` - List categories
- `GET /api/products/featured/` - Featured products

### 🛒 Shopping Cart
- `GET /api/cart/` - Get user cart
- `POST /api/cart/add/` - Add product to cart
- `PUT /api/cart/items/{id}/update/` - Update cart item
- `DELETE /api/cart/items/{id}/remove/` - Remove cart item
- `DELETE /api/cart/clear/` - Clear cart
- `POST /api/cart/validate/` - Validate cart for checkout

### 📦 Orders
- `GET /api/orders/` - List user orders
- `GET /api/orders/{id}/` - Order detail
- `POST /api/orders/create/` - Create new order
- `POST /api/orders/{id}/cancel/` - Cancel order
- `GET /api/orders/track/{order_number}/` - Track order

### 💝 Wishlists
- `GET /api/wishlists/` - List user wishlists
- `POST /api/wishlists/create/` - Create wishlist
- `GET /api/wishlists/{id}/` - Wishlist detail
- `PUT /api/wishlists/{id}/update/` - Update wishlist
- `DELETE /api/wishlists/{id}/delete/` - Delete wishlist
- `POST /api/wishlists/{id}/add-product/` - Add product to wishlist
- `DELETE /api/wishlists/{id}/remove-product/{product_id}/` - Remove product
- `GET /api/wishlists/public/{uuid}/` - Public wishlist by UUID
- `POST /api/wishlists/{id}/favorite/` - Favorite wishlist
- `GET /api/wishlists/favorites/` - List favorite wishlists

## 🗄️ Database Models

### User Model
```python
class User(AbstractUser):
    email = models.EmailField(unique=True)  # Used as username
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
```

### Product Model
```python
class Product(TimestampModelMixin, models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    stock_quantity = models.IntegerField(default=0)
    gallery = models.ForeignKey(Library, on_delete=models.SET_NULL)
```

### Order Model
```python
class Order(TimestampModelMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=50, unique=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    # Shipping information fields...
```

### Wishlist Model
```python
class WishList(TimestampModelMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_public = models.BooleanField(default=False)
    unique_link = models.UUIDField(default=uuid.uuid4, unique=True)
    shipping_data = models.JSONField(blank=True, null=True)
```

## 🔧 Management Commands

The project includes several custom Django management commands for development:

### Generate Fake Data
```bash
# Generate all fake data (recommended)
python manage.py create_fake_data

# Or generate individually:
python manage.py create_fake_users --count 50
python manage.py create_fake_products --count 200
python manage.py create_fake_carts --count 30
python manage.py create_fake_orders --count 100
python manage.py create_fake_wishlists --count 25
```

### Delete Fake Data
```bash
# Remove all fake data (keeps superuser accounts)
python manage.py delete_fake_data --confirm

# Remove all data including superusers
python manage.py delete_fake_data --confirm --no-keep-superusers
```

## 🏪 State Management (Pinia)

### Available Stores
- **authStore** - User authentication and profile management
- **productStore** - Product catalog and search functionality
- **cartStore** - Shopping cart with guest support
- **orderStore** - Order history and tracking
- **wishlistStore** - Wishlist management and favorites

### Usage Example
```javascript
<script setup>
import { useAuthStore, useCartStore } from '@/stores'

const authStore = useAuthStore()
const cartStore = useCartStore()

// Login user
await authStore.login({ email, password })

// Add product to cart
await cartStore.addToCart(productId, quantity)
</script>
```

## 🚦 Frontend Routing

### Public Routes
- `/` - Home page
- `/products` - Product catalog
- `/products/:id` - Product detail
- `/cart` - Shopping cart

### Protected Routes (Require Authentication)
- `/checkout` - Checkout process
- `/orders` - Order history
- `/orders/:id` - Order detail
- `/wishlists` - User wishlists
- `/wishlists/:id` - Wishlist detail
- `/profile` - User profile

### Authentication Routes (Guest Only)
- `/login` - User login
- `/register` - User registration

## 🧪 Development

### Backend Testing
```bash
cd backend
python manage.py test
```

### Frontend Testing
```bash
cd frontend
npm run test
```

### Code Linting
```bash
# Backend (flake8)
cd backend
flake8 .

# Frontend (ESLint)
cd frontend
npm run lint
```

## 🐳 Docker Support

The project includes Docker configuration for easy deployment:

```bash
# Build and run with Docker Compose
docker-compose up --build

# Run in production
docker-compose -f docker-compose.prod.yml up --build
```

## 🌐 Environment Variables

### Backend (.env)
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOWED_ORIGINS=http://localhost:5173
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
GOOGLE_OAUTH2_CLIENT_ID=your-google-client-id
```

### Frontend (.env)
```env
VITE_API_BASE_URL=http://localhost:8000/api
VITE_APP_NAME=BuyItMe
```

## 📚 Technologies Used

### Backend
- **Django 5.1.4** - Web framework
- **Django REST Framework** - API development
- **Simple JWT** - JWT authentication
- **django-cors-headers** - CORS handling
- **django-attachments** - File upload management
- **Pillow** - Image processing
- **Faker** - Fake data generation

### Frontend
- **Vue.js 3.5.13** - Progressive JavaScript framework
- **Pinia 3.0.3** - State management
- **Vue Router 4.5.1** - Client-side routing
- **Axios 1.11.0** - HTTP client
- **Vite 6.3.5** - Build tool and dev server

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Carlos Brito** - [carlos18bp](https://github.com/carlos18bp)

## 🙏 Acknowledgments

- Based on previous projects: [gym_project](https://github.com/carlos18bp/gym_project), [base_feature](https://github.com/carlos18bp/base_feature), [candle_project](https://github.com/carlos18bp/candle_project)
- Django REST Framework documentation
- Vue.js and Pinia teams for excellent documentation
- The open-source community for inspiration and tools

---

<div align="center">
  <p>⭐ Star this repository if you find it helpful!</p>
  <p>Made with ❤️ by <a href="https://github.com/carlos18bp">Carlos Brito</a></p>
</div>