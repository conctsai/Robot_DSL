from engine.variable_manager import VariableManager
import pytest as ptt
from error.dsl_runtime_error import VariableNotDefinedError

class TestVariableManager:
    def test_set_get_variable(self):
        vm = VariableManager()
        vm.set("name", "Tom")
        assert vm.get("name") == "Tom"
        
    def test_get_variable_error(self):
        vm = VariableManager()
        with ptt.raises(VariableNotDefinedError):
            vm.get("name")
        
    def test_set_variable_twice(self):
        vm = VariableManager()
        vm.set("name", "Tom")
        vm.set("name", "Jerry")
        assert vm.get("name") == "Jerry"

    def test_placeholder_format(self):
        vm = VariableManager()
        vm.set("name", "Tom")
        assert vm.format_placeholders("Hello, {name}") == "Hello, Tom"
        
    def test_placeholder_format_error(self):
        vm = VariableManager()
        with ptt.raises(VariableNotDefinedError):
            vm.format_placeholders("Hello, {name}")