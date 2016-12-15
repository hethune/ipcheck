#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/ipcheck/")

from ipcheck import app as application
application.secret_key = '\xd0\x9f;\xee\x14U!\xaa\x88\x07\x1fC\xe4\x01\xed42,\t\x11\x8e!\xc0#'