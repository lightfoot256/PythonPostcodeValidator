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
    output_file = "failed_validation.csv"

    def do_import(self, import_file):
        """ Run the validation against lines in the import file,
        output invalid postcodes to the failed_validation.csv """

        # Create the validator to be used against all post codes
        validator = PostcodeValidator()

        # Open the output file for writing invalid post codes to
        with open(self.output_file, "wt") as output:

            # Create the CSV writer against the output file
            writer = csv.writer(output, delimiter=' ')

            # Write the CSV header row
            writer.writerow(["row_id", "postcode"])

            # Using gzip; open the given file (read text, not append)
            with gzip.open(import_file, mode="rt") as f:

                # Get the csv reader for the unzipped file
                reader = csv.reader(f)

                # Skip the first line which is the header row
                next(reader, None)

                # Iterate over each line in the source file
                for line in reader:

                    # Get the row_id and postcode fields from each line
                    row_id = line[self.import_column_row_id]
                    postcode = line[self.import_column_postcode]

                    # Validate the postcode
                    if not(validator.match(postcode)):

                        # Report on invalid post codes
                        print("Failed to import :", row_id, " (invalid postcode: ", postcode, ")")

                        # Write to the failed output
                        writer.writerow([row_id, postcode])

# Default behaviour when run from command line
if __name__ == '__main__':

    # Create a new importer
    importer = PostcodeImporter()

    # Make sure we have an argument (1 for the command, 1 for the file to import
    if len(sys.argv) == 2:

        # Begin import using second argument (first is command)
        importer.do_import(sys.argv[1])
    else:

        # Show usage
        print("usage: python -m src.postcode_importer [input.gz]")
