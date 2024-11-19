from error.dsl_runtime_error import VariableNotDefinedError

class VariableManager:
    def __init__(self):
        self.variables = {}
        
    def set(self, key, value):
        self.variables[key] = value
        
    def get(self, key):
        if key in self.variables:
            return self.variables[key]
        else:
            raise VariableNotDefinedError("Variable {} not defined".format(key))
        
    def format_placeholders(self, string: str):
        try:
            return string.format(**self.variables)
        except KeyError as e:
            raise VariableNotDefinedError("Variable {} not defined".format(str(e)))
    
    def __str__(self):
        return str(self.variables)
    
    
if __name__ == '__main__':
    vm = VariableManager()
    vm.set("a", 10)
    vm.set("a", 20)
    print(vm.format_placeholders("a is {ba}"))
    