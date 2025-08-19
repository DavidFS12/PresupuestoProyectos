from decouple import config
import dj_database_url

INSTALLED_APPS = [
    ...,
    'rest_framework',
    'core',
]

DATABASES = {
    'default': dj_database_url.parse(config('DATABASE_URL'))
}

