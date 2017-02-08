
import gzip
import csv

from src.postcode_validator import PostcodeValidator

class PostcodeImporter:

    importFile = "../data/import_data.csv.gz"
    importColumnRowId = 0
    importColumnPostCode = 1

    outputFile = "failed_validation.csv"

    def Import(self):

        validator = PostcodeValidator()

        with open(self.outputFile, "wt") as output:
            writer = csv.writer(output, delimiter=' ')
            writer.writerow(["row_id", "postcode"])

            with gzip.open(self.importFile, mode="rt") as f:

                reader = csv.reader(f)
                next(reader, None) # Skip header

                for line in reader:

                    rowId = line[self.importColumnRowId]
                    postcode = line[self.importColumnPostCode]

                    if not(validator.Match(postcode)):

                        print("Failed to import :", rowId, " (invalid postcode: ", postcode , ")");

                        writer.writerow([rowId, postcode])


if __name__ == '__main__':

    importer = PostcodeImporter()

    importer.Import()

