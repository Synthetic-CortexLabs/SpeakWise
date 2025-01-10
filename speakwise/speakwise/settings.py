// ...existing code...

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'speakwise_db',  # Your database name
        'USER': 'postgres',      # Your PostgreSQL username
        'PASSWORD': '',          # Your PostgreSQL password
        'HOST': 'localhost',     # Host where PostgreSQL is running
        'PORT': '5432',         # Default PostgreSQL port
    }
}
