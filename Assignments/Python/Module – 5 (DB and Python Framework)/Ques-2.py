# q.2 How to check installed version of django?


"""
django-admin --version

or

pip list

or

pip show django
"""

#or

import django
print(django.get_version())