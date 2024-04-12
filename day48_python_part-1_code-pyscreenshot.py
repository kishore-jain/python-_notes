# python program pyscreenshot to take screenshot.
# -----------------------------------------------

import pyscreenshot as ps

img = ps.grab()

img.show()

img.save("ss.jpg")
