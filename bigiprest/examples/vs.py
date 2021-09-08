# External Imports
# Import only with "import package",
# it will make explicity in the code where it came from.
import getpass
import os
import hashlib

# Internal imports
# Import only with "from x import y", to simplify the code.
from bigrest.bigip import BIGIP
from bigrest.utils.utils import rest_format
from bigrest.utils.utils import token

device = BIGIP("192.168.86.57", "admin", "W3lcome098!")

virtuals = device.load("/mgmt/tm/ltm/virtual")
for virtual in virtuals:
    print(virtual.properties["name"])
    print(virtual.properties["partition"])
    print(virtual.properties["fullPath"])
    print(virtual.properties["destination"])
    print(virtual.properties["pool"])
