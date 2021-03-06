import unittest
import os
from acme_diags.acme_parameter import ACMEParameter
from acme_diags.acme_diags_driver import _get_default_diags, make_parameters


class TestACMEDriver(unittest.TestCase):
    def setUp(self):
        self.parameter = ACMEParameter()

    def test_get_default_diags(self):
        set_dict = _get_default_diags('5')
        self.assertTrue(set_dict.has_key('set5'))
        self.assertEqual(set_dict['set5'][0]['sets'], [5])

    def test_make_parameters_with_multiple_sets(self):
        self.parameter.sets = ['5', '7']
        self.parameter.reference_data_path = '/'
        self.parameter.test_data_path = '/'
        params = make_parameters(self.parameter)
        self.assertTrue(len(params) > 100)  # since no single run is greater than than 100

if __name__ == '__main__':
    unittest.main()
