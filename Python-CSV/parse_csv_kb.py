import csv

with open('kb11.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_kb11.csv', 'w') as new_file:
        fieldnames = ['Datum splatnosti', 'castka']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
