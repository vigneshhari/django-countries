#!/usr/bin/env python

import os
import sys

from django.conf import settings
import django


DEFAULT_SETTINGS = dict(
    INSTALLED_APPS=(
        'countries_flavor',
        'tests',
    ),
    DATABASES={
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USER'],
            'PASSWORD': os.environ['DB_PASSWORD']
        }
    }
)


def runtests():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)

    django.setup()

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    from django.test.runner import DiscoverRunner
    runner_class = DiscoverRunner
    test_args = ['tests']

    failures = runner_class(
        verbosity=1,
        interactive=True,
        failfast=False)\
        .run_tests(test_args)

    sys.exit(failures)


if __name__ == '__main__':
    runtests()