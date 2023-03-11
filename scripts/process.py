import csv
import sys
import ctypes as ct

# See https://stackoverflow.com/a/54517228 for more info on this
csv.field_size_limit(int(ct.c_ulong(-1).value // 2))

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(output_file, "w", newline="") as csv_out:
    csvwriter = csv.writer(
        csv_out, delimiter="\t", quotechar="|", quoting=csv.QUOTE_MINIMAL
    )

    with open(input_file, "r") as csv_in:
        csvreader = csv.reader(csv_in, delimiter="\t")
        for row in csvreader:
            if len(row) > 4:
                csvwriter.writerow([row[0], row[1], row[2], row[3], row[4]])
