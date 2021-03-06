# Analysis

## Part 1 - Postcode validation

The following regular expression was provided to validate post codes:
>
    (GIR\s0AA) |
    (
        # A9 or A99 prefix
        ( ([A-PR-UWYZ][0-9][0-9]?) |
             # AA99 prefix with some excluded areas
            (([A-PR-UWYZ][A-HK-Y][0-9](?<!(BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WC|WN|ZE)[0-9])[0-9]) |
             # AA9 prefix with some excluded areas
             ([A-PR-UWYZ][A-HK-Y](?<!AB|LL|SO)[0-9]) |
             # WC1A prefix
             (WC[0-9][A-Z]) |
             (
                # A9A prefix
               ([A-PR-UWYZ][0-9][A-HJKPSTUW]) |
                # AA9A prefix
               ([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY])
             )
            )
          )
          # 9AA suffix
        \s[0-9][ABD-HJLNP-UW-Z]{2}
        )

### Verification
Based on [Wikipedia](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Validation) - the validation format is expressed as follows (*where **A** signifies a letter and **9** a digit*);

* **AA9A 9AA** - WC postcode area; EC1–EC4, NW1W, SE1P, SW1 (Example: *EC1A 1BB*)
* **A9A 9AA** - E1W, N1C, N1P (Example: *W1A 0AX*)
* **A9 9AA** - B, E, G, L, M, N, S, W (Example: *M1 1AE*)
* **A99 9AA** -  B, E, G, L, M, N, S, W  (Example: *B33 8TH*)
* **AA9 9AA** - All other postcodes (Example: *CR2 6XH* )
* **AA99 9AA** - All other postcodes (Example: *DN55 1PT*)

On top of this there's a few notes that define some edge cases;

Notes:

* As all formats end with 9AA, the first part of a postcode can easily be extracted by ignoring the last three characters
* Areas with only single-digit districts: BR, FY, HA, HD, HG, HR, HS, HX, JE, LD, SM, SR, WC, WN, ZE (although WC is always subdivided by a further letter, e.g. WC1A).
* Areas with only double-digit districts: AB, LL, SO.
* Areas with a district '0' (zero): BL, BS, CM, CR, FY, HA, PR, SL, SS (BS is the only area to have both a district 0 and a district 10).
* The following central London single-digit districts have been further divided by inserting a letter after the digit and before the space: EC1–EC4 (but not EC50), SW1, W1, WC1, WC2, and part of E1 (E1W), N1 (N1C and N1P), NW1 (NW1W) and SE1 (SE1P).
* The letters QVX are not used in the first position.
* The letters IJZ are not used in the second position.
* The only letters to appear in the third position are ABCDEFGHJKPSTUW when the structure starts with A9A.
* The only letters to appear in the fourth position are ABEHMNPRVWXY when the structure starts with AA9A.
* The final two letters do not use the letters CIKMOV, so as not to resemble digits or each other when hand-written.
* Post code sectors are one of ten digits: 0 to 9 with 0 only used once 9 has been used in a post town, save for Croydon and Newport (see above).

###Confirmation using tests provided

Provided with the regular expression was a series of validation tests; a test case was written in Python to execute these tests and all tests pass proving the regular expression correctly matches postcodes defined in the test

###Validation of all UK postcode cases

A review of the regular expression was carried out:

* As all formats end with 9AA, the first part of a postcode can easily be extracted by ignoring the last three characters

> This part of the regular expression handles the 9AA at the end:

>           # 9AA suffix
        \s[0-9][ABD-HJLNP-UW-Z]{2}


* Areas with only single-digit districts: BR, FY, HA, HD, HG, HR, HS, HX, JE, LD, SM, SR, WC, WN, ZE (although WC is always subdivided by a further letter, e.g. WC1A).

> The part of the regular expression handles single digit districts; excluding the double digit districts from validating in this part:

>              # AA9 prefix with some excluded areas
             ([A-PR-UWYZ][A-HK-Y](?<!AB|LL|SO)[0-9]) |

* Areas with only double-digit districts: AB, LL, SO.

> The following handles double districts; and excludes all the single disticts from appearing here

>              # AA99 prefix with some excluded areas
            (([A-PR-UWYZ][A-HK-Y][0-9](?<!(BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WC|WN|ZE)[0-9])[0-9]) |

* Areas with a district '0' (zero): BL, BS, CM, CR, FY, HA, PR, SL, SS (BS is the only area to have both a district 0 and a district 10).

> **There's nothing specific in the regular expression to catch this particular note**

* The following central London single-digit districts have been further divided by inserting a letter after the digit and before the space: EC1–EC4 (but not EC50), SW1, W1, WC1, WC2, and part of E1 (E1W), N1 (N1C and N1P), NW1 (NW1W) and SE1 (SE1P).

> The following part of the regular expression handles all of those cases

>             # WC1A prefix
             (WC[0-9][A-Z]) |
             (
                # A9A prefix
               ([A-PR-UWYZ][0-9][A-HJKPSTUW]) |
                # AA9A prefix
               ([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY])
             )



* The letters QVX are not used in the first position.

> This is handled by the following:

>     [A-PR-UWYZ]

> Which handles the range A-Z but skips the QVX characters in the sequence; it could have also been written as:

>     [A-Z-[QVX]]

* The letters IJZ are not used in the second position.

> This appears throughout each of the formats as:

>     [A-HK-Y]

* The only letters to appear in the third position are ABCDEFGHJKPSTUW when the structure starts with A9A.

> This is handled here:

>                # A9A prefix
               ([A-PR-UWYZ][0-9][A-HJKPSTUW]) |

* The only letters to appear in the fourth position are ABEHMNPRVWXY when the structure starts with AA9A.

> And here:

>                 # AA9A prefix
               ([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY])


* The final two letters do not use the letters CIKMOV, so as not to resemble digits or each other when hand-written.

> Again the final parrt skips these letters in the various ranges:

>           # 9AA suffix
        \s[0-9][ABD-HJLNP-UW-Z]{2}

* Post code sectors are one of ten digits: 0 to 9 with 0 only used once 9 has been used in a post town, save for Croydon and Newport (see above).

> This is not covered by the regular expression


# Performance

## Measurement

* Running cProfile against the import script shows a total time of about 22 seconds; See [output](UNOPTIMISED_CPROFILE.md)
* 12 seconds (60%) of this time is spent "reporting" the failed results to the console

## Optimisations
### Removing the output 

Removing the print function yields a 60% reduction in speed as noted by the profiler [output](OPTIMISED_CPROFILE.md)

### Re-writing the validator in "code"

As an exercise in proving how efficient the compiled regex is; I wrote some [code](src/postcode_validator_without_regex.py) that matches the postcodes enough to pass the 16 existing [tests](tests/postcode_validator_without_regex_test.py) and ran it through the same input data;

The results are shown [Here](WITHOUT_REGEX_CPROFILE.md)

---
## changelog
* 08-Feb-2017 Moved analysis notes from README.md
