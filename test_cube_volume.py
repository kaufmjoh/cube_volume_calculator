import unittest
import cube_volume

class TestCubeVolume(unittest.TestCase):
	def test_integer_volume(self):
		self.assertEqual(cube_volume.volume(2,3,4), 24)
		self.assertEqual(cube_volume.volume(1,1,1), 1)
		self.assertEqual(cube_volume.volume(1,1,0), 0)
		self.assertEqual(cube_volume.volume(1,3,1), 3)


	def test_decimal_inputs(self):
		self.assertEqual(cube_volume.volume(1.0, 1.0, 1.0), 1)
		self.assertEqual(cube_volume.volume(1.2, 1.3, 1.4), 2.184)
		self.assertEqual(cube_volume.volume(0.5, 0.6, 0.7), 0.21)
		self.assertEqual(cube_volume.volume(.5, .6, .7), .21)

	def test_bad_input(self):
		self.assertEqual(cube_volume.volume(-1,2,3), "At least one of your inputs was invalid.")
		self.assertEqual(cube_volume.volume(2,-1,3), "At least one of your inputs was invalid.")
		self.assertEqual(cube_volume.volume(3,2,-1), "At least one of your inputs was invalid.")
		self.assertEqual(cube_volume.volume(3,-2,"1c"), "At least one of your inputs was invalid.")
		self.assertEqual(cube_volume.volume("3a","2b",-1), "At least one of your inputs was invalid.")
		self.assertEqual(cube_volume.volume("Bad input",-2,-1), "At least one of your inputs was invalid.")
		self.assertEqual(cube_volume.volume(3,2,"Bad input"), "At least one of your inputs was invalid.")

if __name__ == '__main__':
	unittest.main()
