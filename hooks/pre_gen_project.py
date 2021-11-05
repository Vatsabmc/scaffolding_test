"""
Pre Cookie Generation script(s)
If any error is raised, the cookie cutter creation fails and crashes
"""

import re
import sys
import datetime

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
EMAIL_REGEX = r'[^@]+@[^@]+\.[^@]+'
DATE_FORMAT= "%Y-%m-d"

email = '{{ cookiecutter.email }}'
release_date = '{{ cookiecutter.release_date }}'

if not re.match(EMAIL_REGEX, email):
    print(f'ERROR: email: {email} no es una dirección de correo valida.')
    sys.exit(1)

