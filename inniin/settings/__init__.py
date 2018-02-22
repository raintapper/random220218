
from .base import *

from .production import *

try:
   from .local import *
except:
   pass


#ordering is important ^^ above means local will be called if local exist. 
#If it is not called, production is called
#If it is not called, base is called

