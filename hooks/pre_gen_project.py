"""
Pre Cookie Generation script(s)
If any error is raised, the cookie cutter creation fails and crashes
"""

import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
EMAIL_REGEX = r'[^@]+@[^@]+\.[^@]+'

author_email = '{{ cookiecutter.email }}'

if not re.match(EMAIL_REGEX, author_email):
    print('ERROR: "{}" no es una dirección de correo valida!'.format(author_email))

    # exits with status 1 to indicate failure
    sys.exit(1)
