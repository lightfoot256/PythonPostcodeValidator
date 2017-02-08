import unittest

from src.postcode_validator import PostcodeValidator

class PostcodeValidationTest(unittest.TestCase):

    def setUp(self):
        self.postcodeValidator = PostcodeValidator();

    def tearDown(self):
        pass

    def test_Junk(self):
        self.assertFalse(self.postcodeValidator.Match('$%± ()()'));
    def test_Invalid(self):
        self.assertFalse(self.postcodeValidator.Match('XX XXX'));
    def test_Incorrect_inward_code_length(self):
        self.assertFalse(self.postcodeValidator.Match('A1 9A'));
    def test_No_space(self):
        self.assertFalse(self.postcodeValidator.Match('LS44PL'));

    def test_Q_in_first_position(self):
        self.assertFalse(self.postcodeValidator.Match('Q1A 9AA'));
    def test_V_in_first_position(self):
        self.assertFalse(self.postcodeValidator.Match('V1A 9AA'));
    def test_X_in_first_position(self):
        self.assertFalse(self.postcodeValidator.Match('X1A 9BB'));

    def test_I_in_second_position(self):
        self.assertFalse(self.postcodeValidator.Match('LI10 3QP'));
    def test_J_in_second_position(self):
        self.assertFalse(self.postcodeValidator.Match('LJ10 3QP'));
    def test_Z_in_second_position(self):
        self.assertFalse(self.postcodeValidator.Match('LZ10 3QP'));

    def test_Q_in_third_position_with_A9A_structure(self):
        self.assertFalse(self.postcodeValidator.Match('A9Q 9AA'));

    def test_C_in_fourth_position_with_AA9A_structure(self):
        self.assertFalse(self.postcodeValidator.Match('AA9C 9AA'));

    def test_Area_with_only_single_digit_districts(self):
        self.assertFalse(self.postcodeValidator.Match('FY10 4PL'));
    def test_Area_with_only_double_digit_districts(self):
        self.assertFalse(self.postcodeValidator.Match('SO1 4QQ'));

    def test_Valid(self):
        self.assertTrue(self.postcodeValidator.Match('EC1A 1BB'));
        self.assertTrue(self.postcodeValidator.Match('W1A 0AX'));
        self.assertTrue(self.postcodeValidator.Match('M1 1AE'));
        self.assertTrue(self.postcodeValidator.Match('B33 8TH'));
        self.assertTrue(self.postcodeValidator.Match('CR2 6XH'));
        self.assertTrue(self.postcodeValidator.Match('DN55 1PT'));
        self.assertTrue(self.postcodeValidator.Match('GIR 0AA'));
        self.assertTrue(self.postcodeValidator.Match('SO10 9AA'));
        self.assertTrue(self.postcodeValidator.Match('FY9 9AA'));
        self.assertTrue(self.postcodeValidator.Match('WC1A 9AA'));


    def test_Custom(self):
        self.assertTrue(self.postcodeValidator.Match('BL0 4QQ'));
        self.assertTrue(self.postcodeValidator.Match('BL10 4QQ'));


if __name__ == '__main__':
    unittest.main();

