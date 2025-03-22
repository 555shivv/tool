# Copyright: copyright.txt

'''import inspect
import re
import os
import sys
from .invocation import FunctionInvocation
from .symbolic_types import SymbolicInteger, getSymbolic

# The built-in definition of len wraps the return value in an int() constructor, destroying any symbolic types.
# By redefining len here we can preserve symbolic integer types.
import builtins
builtins.len = (lambda x : x.__len__())

class Loader:
	def __init__(self, filename, entry):
		self._fileName = os.path.basename(filename)
		self._fileName = self._fileName[:-3]
		if (entry == ""):
			self._entryPoint = self._fileName
		else:
			self._entryPoint = entry;
		self._resetCallback(True)

	def getFile(self):
		return self._fileName

	def getEntry(self):
		return self._entryPoint
	
	def createInvocation(self):
		inv = FunctionInvocation(self._execute,self._resetCallback)
		func = self.app.__dict__[self._entryPoint]
		argspec = inspect.getargspec(func)
		# check to see if user specified initial values of arguments
		if "concrete_args" in func.__dict__:
			for (f,v) in func.concrete_args.items():
				if not f in argspec.args:
					print("Error in @concrete: " +  self._entryPoint + " has no argument named " + f)
					raise ImportError()
				else:
					Loader._initializeArgumentConcrete(inv,f,v)
		if "symbolic_args" in func.__dict__:
			for (f,v) in func.symbolic_args.items():
				if not f in argspec.args:
					print("Error (@symbolic): " +  self._entryPoint + " has no argument named " + f)
					raise ImportError()
				elif f in inv.getNames():
					print("Argument " + f + " defined in both @concrete and @symbolic")
					raise ImportError()
				else:
					s = getSymbolic(v)
					if (s == None):
						print("Error at argument " + f + " of entry point " + self._entryPoint + " : no corresponding symbolic type found for type " + str(type(v)))
						raise ImportError()
					Loader._initializeArgumentSymbolic(inv, f, v, s)
		for a in argspec.args:
			if not a in inv.getNames():
				Loader._initializeArgumentSymbolic(inv, a, 0, SymbolicInteger)
		return inv

	# need these here (rather than inline above) to correctly capture values in lambda
	def _initializeArgumentConcrete(inv,f,val):
		inv.addArgumentConstructor(f, val, lambda n,v: val)

	def _initializeArgumentSymbolic(inv,f,val,st):
		inv.addArgumentConstructor(f, val, lambda n,v: st(n,v))

	def executionComplete(self, return_vals):
		if "expected_result" in self.app.__dict__:
			return self._check(return_vals, self.app.__dict__["expected_result"]())
		if "expected_result_set" in self.app.__dict__:
			return self._check(return_vals, self.app.__dict__["expected_result_set"](),False)
		else:
			print(self._fileName + ".py contains no expected_result function")
			return None

	# -- private

	def _resetCallback(self,firstpass=False):
		self.app = None
		if firstpass and self._fileName in sys.modules:
			print("There already is a module loaded named " + self._fileName)
			raise ImportError()
		try:
			if (not firstpass and self._fileName in sys.modules):
				del(sys.modules[self._fileName])
			self.app =__import__(self._fileName)
			if not self._entryPoint in self.app.__dict__ or not callable(self.app.__dict__[self._entryPoint]):
				print("File " +  self._fileName + ".py doesn't contain a function named " + self._entryPoint)
				raise ImportError()
		except Exception as arg:
			print("Couldn't import " + self._fileName)
			print(arg)
			raise ImportError()

	def _execute(self, **args):
		return self.app.__dict__[self._entryPoint](**args)

	def _toBag(self,l):
		bag = {}
		for i in l:
			if i in bag:
				bag[i] += 1
			else:
				bag[i] = 1
		return bag

	def _check(self, computed, expected, as_bag=True):
		b_c = self._toBag(computed)
		b_e = self._toBag(expected)
		if as_bag and b_c != b_e or not as_bag and set(computed) != set(expected):
			print("-------------------> %s test failed <---------------------" % self._fileName)
			print("Expected: %s, found: %s" % (b_e, b_c))
			return False
		else:
			print("%s test passed <---" % self._fileName)
			return True
	
def loaderFactory(filename,entry):
	if not os.path.isfile(filename) or not re.search(".py$",filename):
		print("Please provide a Python file to load")
		return None
	try: 
		dir = os.path.dirname(filename)
		sys.path = [ dir ] + sys.path
		ret = Loader(filename,entry)
		return ret
	except ImportError:
		sys.path = sys.path[1:]
		return None '''
		
		

###########################################################
import inspect
import re
import os
import sys
from .invocation import FunctionInvocation
from .symbolic_types import SymbolicInteger, getSymbolic

# Preserve symbolic types for len()
import builtins
builtins.len = (lambda x: x.__len__())


class Loader:
    def __init__(self, filename, entry):
        self._fileName = os.path.basename(filename)
        self._fileName = self._fileName[:-3]  # Remove ".py"
        self._entryPoint = entry if entry else None
        self._resetCallback(True)

    def getFile(self):
        return self._fileName

    def getEntry(self):
        return self._entryPoint

    def createInvocation(self):
        inv = FunctionInvocation(self._execute, self._resetCallback)
        if self._entryPoint:
            func = self.app.__dict__[self._entryPoint]
            argspec = inspect.getfullargspec(func)

            # Handle concrete arguments
            if "concrete_args" in func.__dict__:
                for f, v in func.concrete_args.items():
                    if f not in argspec.args:
                        raise ImportError(f"Error in @concrete: {self._entryPoint} has no argument named {f}")
                    self._initializeArgumentConcrete(inv, f, v)

            # Handle symbolic arguments
            if "symbolic_args" in func.__dict__:
                for f, v in func.symbolic_args.items():
                    if f not in argspec.args:
                        raise ImportError(f"Error (@symbolic): {self._entryPoint} has no argument named {f}")
                    elif f in inv.getNames():
                        raise ImportError(f"Argument {f} defined in both @concrete and @symbolic")
                    else:
                        s = getSymbolic(v)
                        if s is None:
                            raise ImportError(f"Error at argument {f}: No corresponding symbolic type for {type(v)}")
                        self._initializeArgumentSymbolic(inv, f, v, s)

            # Initialize remaining arguments as symbolic
            for a in argspec.args:
                if a not in inv.getNames():
                    self._initializeArgumentSymbolic(inv, a, 0, SymbolicInteger)

        return inv

    def executionComplete(self, return_vals):
        if "expected_result" in self.app.__dict__:
            return self._check(return_vals, self.app.expected_result())
        if "expected_result_set" in self.app.__dict__:
            return self._check(return_vals, self.app.expected_result_set(), False)
        print(f"{self._fileName}.py contains no expected_result function")
        return None

    def _resetCallback(self, firstpass=False):
        self.app = None
        if firstpass and self._fileName in sys.modules:
            raise ImportError(f"Module {self._fileName} is already loaded")

        try:
            if not firstpass and self._fileName in sys.modules:
                del sys.modules[self._fileName]
                
            self.app = __import__(self._fileName)

            # If no valid function found, execute entire script
            if self._entryPoint and self._entryPoint not in self.app.__dict__:
                print(f"Warning: No function '{self._entryPoint}' found in {self._fileName}. Running entire script.")
                self._entryPoint = None

        except Exception as e:
            print(f"Error importing {self._fileName}: {e}")
            raise ImportError()

    def _execute(self, **args):
        if self._entryPoint:
            return self.app.__dict__[self._entryPoint](**args)
        return None  # Entire script executes normally without needing a function call

    def _toBag(self, lst):
        bag = {}
        for i in lst:
            bag[i] = bag.get(i, 0) + 1
        return bag

    def _check(self, computed, expected, as_bag=True):
        if as_bag and self._toBag(computed) != self._toBag(expected) or not as_bag and set(computed) != set(expected):
            print(f"------> {self._fileName} test failed <------")
            print(f"Expected: {expected}, Found: {computed}")
            return False
        print(f"{self._fileName} test passed <---")
        return True

    @staticmethod
    def _initializeArgumentConcrete(inv, f, val):
        inv.addArgumentConstructor(f, val, lambda n, v: val)

    @staticmethod
    def _initializeArgumentSymbolic(inv, f, val, st):
        inv.addArgumentConstructor(f, val, lambda n, v: st(n, v))


def loaderFactory(filename, entry=None):
    if not os.path.isfile(filename) or not filename.endswith(".py"):
        print("Error: Please provide a valid Python file.")
        return None

    try:
        dir_path = os.path.dirname(filename)
        sys.path.insert(0, dir_path)  # Add script directory to sys.path
        loader = Loader(filename, entry)

        # If entry function is missing, execute the entire script
        if entry and entry not in loader.app.__dict__:
            print(f"Warning: No function '{entry}' found in {filename}. Running entire script.")
            loader._entryPoint = None

        return loader

    except ImportError:
        sys.path.pop(0)  # Remove added path on failure
        return None

