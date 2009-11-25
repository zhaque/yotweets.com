### -*- coding: utf-8 -*- ####################################################

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

install_requires = [
        'setuptools',
        'Django',
        'django-compress',
        'django-extensions',
        'django-perfect404',
        'django-templatesadmin',
        'app_media',
        'django-paypal',
        'django-paypal-api',
        'django-twitter-oauth',
        'django-shorturls',
        'South',
        'Fabric',
        'PIL',
        'simplejson',
        'saaskit-prepaid',
        'django-tasks',
        'django-uni-form',
	'django-oembed',
	'django-tagging',
]

extras_require = dict(
    test = [
        'coverage',
        'windmill',
    ]
)

#AFAIK:
install_requires.extend(extras_require['test'])


dependency_links = [
        'http://pypi.saaskit.org/Fabric/',
        'http://pypi.saaskit.org/South/',
        'http://pypi.saaskit.org/app-media/',
        'http://pypi.saaskit.org/django-paypal/',
        'http://pypi.saaskit.org/django-paypal-api/',
        'http://pypi.saaskit.org/django-twitter-oauth/',
        'http://pypi.saaskit.org/django-shorturls/',
        'http://pypi.saaskit.org/django-uni-form/', 
        'http://pypi.pinaxproject.com/',
]

setup(name="yotweets",
            version="0.1",
            description="yotweets Webapp",
            author="CrowdSense",
            author_email="admin@yotweets.com",
            packages = find_packages('src'),
            package_dir = {'': 'src'},
            include_package_data = True,
            zip_safe = False,
            install_requires = install_requires,
            extras_require = extras_require,
            entry_points="""
              # -*- Entry points: -*-
              """,
            dependency_links = dependency_links,
)
