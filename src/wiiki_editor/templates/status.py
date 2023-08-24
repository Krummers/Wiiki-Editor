class Status(object):
    
    def __init__(self, status, variable = None):
        """
        0. No
        1. Yes
        2. Maybe
        """
        if status not in range(3):
            raise ValueError("only status 0, 1 and 2 are accepted")
        self.status = status
        self.variable = variable
    
    def __str__(self):
        if self.status == 0 and self.variable:
            return "{{no|" + str(self.variable) + "}}"
        elif self.status == 1 and self.variable:
            return "{{yes|" + str(self.variable) + "}}"
        elif self.status == 2 and self.variable:
            return "{{maybe|" + str(self.variable) + "}}"
        elif self.status == 0:
            return "{{no}}"
        elif self.status == 1:
            return "{{yes}}"
        elif self.status == 2:
            return "{{maybe}}"
    
    def __repr__(self):
        return str(self)
