class Check:
    def __init__(self, name, description, check_function):
      self.name = name
      self.description = description
      self.check_function = check_function
    def checkForDupes(self, table):
      if len(table) != len(set(table)):
        return False