import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


# import os
# from static_ranges import Ranges
# from dj_static import Cling, MediaCling
# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')
# # application = get_wsgi_application()
# application = Ranges(Cling(MediaCling(get_wsgi_application())))