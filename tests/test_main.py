import unittest

class TestStartServer(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testA(self):
		pass

	# No file name is an error
	# Non-existant file is an error
	# Tsunami-udp non-existant on source machine is an error
    # Returns port number of started server
    # If a server is running on the first tried port, it will start on the second
    # If a server is running on all ports in the range, raise an error
	


class TestReceiveFile(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testA(self):
		pass

    # No source file name is an error
    # No destination file name is an erro
    # No port is an error
    # Non-existant source file is an error
    # Non-existant destination directory is an error
    # Port <1 is an error
    # Tsunami-udp non-existant on destination machine is an error
    # Destination is a file
    # Destination is a directory
    # Destination defines a bad port
    # Destination defines a good port
    # Destination defines a bad machine
    # Destination defines a good machine
    # Destination defines a bad user
    # Destination defines a good user
    # Returns 0 for good transfer
    # Returns >0 for bad transfer
    # Dry run returns 0 for good transfer, file is not copied
    # Dry run returns >1 for bad transfer

if __name__ == "__main__":
    unittest.main()

