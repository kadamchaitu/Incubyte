import unittest
from chandrayaan3_task import Chandrayaan_mission

class TestsOfChandrayaan3(unittest.TestCase):
    # Existing test

    def test_move_forward(self):
        chandra = Chandrayaan_mission()
        chandra.movement('f','N')
        self.assertEqual(chandra.getPos(), [0, 1, 0])

    def test_move_backward(self):
        chandra = Chandrayaan_mission()
        chandra.movement('b','N')
        self.assertEqual(chandra.getPos(), [0, -1, 0])

    def test_turn_left(self):
        chandra = Chandrayaan_mission()
        chandra.turning('l','N')
        self.assertEqual(chandra.getDirection(), 'W')

    def test_turn_right(self):
        chandra = Chandrayaan_mission()
        chandra.turning('r','E')
        self.assertEqual(chandra.getDirection(), 'S')

    def test_tilt_up(self):
        chandra = Chandrayaan_mission()
        chandra.tilted('u','N')
        self.assertEqual(chandra.getDirection(), 'U')

    def test_tilt_down(self):
        chandra = Chandrayaan_mission()
        chandra.tilted('d','S')
        self.assertEqual(chandra.getDirection(), 'D')

    def test_sequence_of_commands(self):
        chandra = Chandrayaan_mission()
        commands = ['u', 'b', 'f', 'l', 'r', 'd']
        chandra.execute_orders(commands)
        self.assertEqual(chandra.getPos(), [0, 0, 0])
        self.assertEqual(chandra.getDirection(), 'D')

        cmd = ['b', 'r', 'f', 'l', 'b', 'u', 'f', 'd']
        chandra.execute_orders(cmd)
        self.assertEqual(chandra.getPos(), [1, -1, 2])
        self.assertEqual(chandra.getDirection(), 'D')

        cmd2 = ['f', 'f', 'u', 'u', 'l', 'l', 'b', 'b']
        chandra.execute_orders(cmd2)
        self.assertEqual(chandra.getPos(), [1, 1, 0])
        self.assertEqual(chandra.getDirection(), 'S')

    def test_sequence_of_commands2(self):
        chandra = Chandrayaan_mission()
        commands = ['u', 'r', 'u', 'b', 'r', 'f', 'l', 'r']
        chandra.execute_orders(commands)
        self.assertEqual(chandra.getPos(), [0, -1, -1])
        self.assertEqual(chandra.getDirection(), 'S')

