
import gzip
import csv
import cProfile

from src.postcode_validator import PostcodeValidator

class PostcodeImporter:

    importFile = "../data/import_data.csv.gz"
    importColumnRowId = 0
    importColumnPostCode = 1

    outputFile = "failed_validation.csv"

    outputFileSuccess = "succeeded_validation.csv"

    def Import(self):

        validator = PostcodeValidator()

        validItems = {}
        invalidItems = {}

        with gzip.open(self.importFile, mode="rt") as f:

            reader = csv.reader(f)

            # Skip header row
            next(reader, None)

            for line in reader:

                rowId = int(line[self.importColumnRowId])
                postcode = line[self.importColumnPostCode]

                if not(validator.Match(postcode)):

                    print("Failed to import :", rowId, " (invalid postcode: ", postcode , ")");

                    invalidItems[rowId] = postcode;

                else:

                    validItems[rowId] = postcode;

        self.WriteItems(self.outputFileSuccess, validItems)
        self.WriteItems(self.outputFile, invalidItems)


    def WriteItems(self, filename, items):

        with open(filename, "wt") as stream:

            writer = csv.writer(stream, delimiter=' ',  lineterminator='\n')
            writer.writerow(["row_id", "postcode"])

            for key in sorted(items.keys()):

                item = items[key]
                writer.writerow([key, item])


if __name__ == '__main__':

    importer = PostcodeImporter()

    cProfile.run('importer.Import()')


