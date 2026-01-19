#packages
# using packages
# method 1: import whole package
import mathpack.basic
print(mathpack.basic.add(5, 3))

# method 2: import module
from mathpack import basic
print(basic.sub(10, 4))

# method 3: import function directly
from mathpack.basic import add
print(add(6, 3))

# absolute import 
from mathpack.basic import add

# relative import
from .basic import sub




