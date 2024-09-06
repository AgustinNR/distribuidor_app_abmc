import re

class Validar:
    def __init__(
        self,
    ):pass

    def regex(self, patron, descripcion):
        if re.match(patron, descripcion):
            return True
        else:
            return False