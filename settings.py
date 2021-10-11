# Authentication parameters
AUTH_USER_MODEL = 'shared_security.User' # shared_security is our SDK package name, this param tell the SDK which user model to use

AUTH_USER_TABLE = 'users_user' # this is the table name in the database for our users model

AUTH_DB = 'primary_db' # this is the name of the database holding the users model

DATABASE_ROUTERS = ['shared_security.dbrouter.AuthRouter']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.getenv('DB_HOST'),
        'PORT': int(os.getenv('DB_PORT', 3306)),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'NAME': os.getenv('DB_NAME')
    },
    'primary_db': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.getenv('DB_HOST'),
        'PORT': int(os.getenv('DB_PORT', 3306)),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'NAME': 'primary',
    }
}
