import unittest

from src.postcode_validator import PostcodeValidator


class PostcodeValidationTest(unittest.TestCase):

    def setUp(self):
        self.postcodeValidator = PostcodeValidator()

    def tearDown(self):
        pass

    def test_Junk(self):
        self.assertFalse(self.postcodeValidator.match('$%± ()()'))

    def test_Invalid(self):
        self.assertFalse(self.postcodeValidator.match('XX XXX'))

    def test_Incorrect_inward_code_length(self):
        self.assertFalse(self.postcodeValidator.match('A1 9A'))

    def test_No_space(self):
        self.assertFalse(self.postcodeValidator.match('LS44PL'))

    def test_Q_in_first_position(self):
        self.assertFalse(self.postcodeValidator.match('Q1A 9AA'))

    def test_V_in_first_position(self):
        self.assertFalse(self.postcodeValidator.match('V1A 9AA'))

    def test_X_in_first_position(self):
        self.assertFalse(self.postcodeValidator.match('X1A 9BB'))

    def test_I_in_second_position(self):
        self.assertFalse(self.postcodeValidator.match('LI10 3QP'))

    def test_J_in_second_position(self):
        self.assertFalse(self.postcodeValidator.match('LJ10 3QP'))

    def test_Z_in_second_position(self):
        self.assertFalse(self.postcodeValidator.match('LZ10 3QP'))

    def test_Q_in_third_position_with_A9A_structure(self):
        self.assertFalse(self.postcodeValidator.match('A9Q 9AA'))

    def test_C_in_fourth_position_with_AA9A_structure(self):
        self.assertFalse(self.postcodeValidator.match('AA9C 9AA'))

    def test_Area_with_only_single_digit_districts(self):
        self.assertFalse(self.postcodeValidator.match('FY10 4PL'))

    def test_Area_with_only_double_digit_districts(self):
        self.assertFalse(self.postcodeValidator.match('SO1 4QQ'))

    def test_Valid(self):
        self.assertTrue(self.postcodeValidator.match('EC1A 1BB'))
        self.assertTrue(self.postcodeValidator.match('W1A 0AX'))
        self.assertTrue(self.postcodeValidator.match('M1 1AE'))
        self.assertTrue(self.postcodeValidator.match('B33 8TH'))
        self.assertTrue(self.postcodeValidator.match('CR2 6XH'))
        self.assertTrue(self.postcodeValidator.match('DN55 1PT'))
        self.assertTrue(self.postcodeValidator.match('GIR 0AA'))
        self.assertTrue(self.postcodeValidator.match('SO10 9AA'))
        self.assertTrue(self.postcodeValidator.match('FY9 9AA'))
        self.assertTrue(self.postcodeValidator.match('WC1A 9AA'))

    def test_Custom(self):
        self.assertTrue(self.postcodeValidator.match('BL0 4QQ'))
        self.assertTrue(self.postcodeValidator.match('BL10 4QQ'))

suite = unittest.TestLoader().loadTestsFromTestCase(PostcodeValidationTest)
unittest.TextTestRunner(verbosity=2).run(suite)
