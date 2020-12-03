import sys
import unittest
import openbadge_analysis as ob


class PortingTests(unittest.TestCase):

    def test_mac_to_id(self):
        """ Confirm new version of mac address conversion to id to match old """
        self.assertEqual(ob.core.mac_address_to_id("FD:99:D9:69:5D:BC"), 1910)


if __name__ == '__main__':
    sys.exit(unittest.main())
