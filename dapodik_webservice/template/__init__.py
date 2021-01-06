import os
import sys

TEMPLATE_DIR = os.path.dirname(os.path.realpath(__file__))

TEMPLATE = os.path.join(TEMPLATE_DIR, "TEMPLATE.xlsx")

if os.path.isfile(TEMPLATE):
    pass
else:
    TEMPLATE_DIR = os.path.dirname(os.path.realpath(sys.executable))
    TEMPLATE = os.path.join(TEMPLATE_DIR, "template", "TEMPLATE.xlsx")
