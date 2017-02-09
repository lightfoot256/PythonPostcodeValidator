#!/usr/bin/env python

""" Optimised Postcode validator; uses regular expression to validate postcodes via the match function """

import re


class PostcodeValidatorWithoutRegex:

    @staticmethod
    def match_number(c):
        return c >= '0' and c <= '9'

    @staticmethod
    def match_AtoPRtoUWYZ(c):
        return (c >= 'A' and c <='Z') and c != 'Q' and c != 'V' and c != 'X'

    @staticmethod
    def match_AtoHKtoY(c):
        return (c >= 'A' and c <='Z') and c != 'I' and c != 'J' and c != 'Z'

    @staticmethod
    def match_AtoHJKPSTUW(c):
        return (c >= 'A' and c <='H') or c == 'J' or c == 'K' or c == 'P' or c == 'S' or c == 'T' or c == 'U' or c == 'W'

    @staticmethod
    def match_ABDtoHJLNPtoUWtoZ(c):
        return (c >= 'A' and c <= 'Z') \
               and c != 'C' \
               and c != 'I' \
               and c != 'K' \
               and c != 'M'  \
               and c != 'O'  \
               and c != 'V'

    @staticmethod
    def match_ABEHMNPRVWXY(c):
        return c == 'A' \
               or c == 'B' \
               or c == 'E' \
               or c == 'H' \
               or c == 'M' \
               or c == 'N' \
               or c == 'P' \
               or c == 'R' \
               or c == 'V' \
               or c == 'W' \
               or c == 'X' \
               or c == 'Y'

    @staticmethod
    def match_suffix(suffix):
        return len(suffix) > 3 and suffix[0] == ' ' and PostcodeValidatorWithoutRegex.match_number(suffix[1]) \
               and PostcodeValidatorWithoutRegex.match_ABDtoHJLNPtoUWtoZ(suffix[2]) \
               and PostcodeValidatorWithoutRegex.match_ABDtoHJLNPtoUWtoZ(suffix[3])

    @staticmethod
    def match_double_district(district):
        return district == 'BR' or \
                district == 'FY' or \
                district == 'HA' or \
                district == 'HD' or \
                district == 'HG' or \
                district == 'HR' or \
                district == 'HS' or \
                district == 'HX' or \
                district == 'JE' or \
                district == 'LD' or \
                district == 'SM' or \
                district == 'SR' or \
                district == 'WC' or \
                district == 'WN' or \
                district == 'ZE'

    @staticmethod
    def match_single_district(district):
        return district == 'AB' or \
                district == 'LL' or \
                district == 'SO'

    def match(self, postcode):

        if( self.match_AtoPRtoUWYZ(postcode[0])):
            if self.match_number(postcode[1]):

                # A99
                if self.match_number(postcode[2]):
                    return self.match_suffix(postcode[3:])

                # A9A
                elif self.match_AtoHJKPSTUW(postcode[2]):
                    return self.match_suffix(postcode[3:])

                # A9
                else:
                    return self.match_suffix(postcode[2:])

            elif self.match_AtoHKtoY(postcode[1]):
                if self.match_number(postcode[2]):

                    # AA99
                    if self.match_number(postcode[3]):
                        if not self.match_double_district(postcode[0:2]):
                            return self.match_suffix(postcode[4:])

                    # AA9A
                    elif self.match_ABEHMNPRVWXY(postcode[3]):
                        return self.match_suffix(postcode[4:])

                    # AA9
                    else:
                        if not self.match_single_district(postcode[0:2]):
                            return self.match_suffix(postcode[3:])

        if postcode[0:3] == 'GIR':
            return self.match_suffix(postcode[3:])

        return False;
