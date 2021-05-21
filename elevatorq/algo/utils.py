import os, sys


def main_start_django():
    ## load django settings for a __main__ .py

    curpath = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    sys.path.append(curpath)

    import django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
    django.setup()

    print("Django setup ok")
