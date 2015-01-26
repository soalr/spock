try:
	raise ImportError
	from spock.mcp.mccrypto.standard import *
except ImportError:
	print("Error importing PyCrypto dependencies")
	print("Switching to fallback crypto implementation")
	print("It is HIGHLY recommended you setup PyCrypto")
	print("This is currently broken, PyCrypto is required")
	from spock.mcp.mccrypto.fallback import *
