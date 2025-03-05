INSTALLED_APPS = [
    'rest_framework',
    'corsheaders',  # Handle frontend requests
    'users',
    'challenges',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True  # Allow frontend to access backend
