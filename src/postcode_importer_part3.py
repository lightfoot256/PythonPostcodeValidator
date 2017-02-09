#!/usr/bin/env python

""" Postcode Importer; writes failed and successful validations of import source postcodes """

import time
import csv
import gzip
import sys

from src.postcode_validator import PostcodeValidator


class PostcodeImporter:

    # The index in the source csv of the column for row id
    import_column_row_id = 0

    # The index in the source csv of the column for row id
    import_column_postcode = 1

    # The filename to output failed postcodes to
    output_file_failed = "failed_validation.csv"

    # The filename to output successful postcodes to
    output_file_success = "succeeded_validation.csv"

    def do_import(self, import_file):
        """ Run the validation against lines in the import file,
        output invalid postcodes to the failed_validation.csv """

        # Create the validator to be used against all post codes
        validator = PostcodeValidator()

        # Initialise a list to hold the valid items
        valid_items = {}

        # Initialise a list to hold the invalid items
        invalid_items = {}

        # Using gzip; open the given file (read text, not append)
        with gzip.open(import_file, mode="rt") as f:

            # Get the csv reader for the unzipped file
            reader = csv.reader(f)

            # Skip the first line which is the header row
            next(reader, None)

            # Iterate over each line in the source file
            for line in reader:

                # Get the row_id and postcode fields from each line
                # Convert to int to ensure sort is int based rather than by string
                row_id = int(line[self.import_column_row_id])
                postcode = line[self.import_column_postcode]

                # Validate the postcode
                if not(validator.match(postcode)):

                    # Report on invalid post codes
                    print("Failed to import :", row_id, " (invalid postcode: ", postcode, ")")

                    # Add the postcode to the invalid list with the row_id as the key
                    invalid_items[row_id] = postcode

                # Postcode is valid
                else:

                    # Add the postcode to the valid list with the row_id as the key
                    valid_items[row_id] = postcode

        # Save all the valid items to file
        self.write_items(self.output_file_success, valid_items)

        # Save all the invalid items to file
        self.write_items(self.output_file_failed, invalid_items)

    @staticmethod
    def write_items(output_file, items):
        """ Given a dictionary of postcodes stored by row_id, store them sorted by row_id to the given filename """

        # Open the output file
        with open(output_file, "wt") as stream:

            # Create a CSV writer for the output
            writer = csv.writer(stream, delimiter=' ',  lineterminator='\n')

            # Add the CSV header
            writer.writerow(["row_id", "postcode"])

            # Iterate over the sorted keys (row_ids)
            for row_id in sorted(items.keys()):

                # Get the postcode
                postcode = items[row_id]

                # Wrie the row_id and postcode
                writer.writerow([row_id, postcode])

# Default behaviour when run from command line
if __name__ == '__main__':

    start = time.time()

    # Create a new importer
    importer = PostcodeImporter()

    # Make sure we have an argument (1 for the command, 1 for the file to import
    if len(sys.argv) == 2:

        # Begin import using second argument (first is command)
        importer.do_import(sys.argv[1])
    else:

        # Show usage
        print("usage: python -m src.postcode_importer [input.gz]")

    end = time.time()

    print("Time taken:", end-start, " seconds")
