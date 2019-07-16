import csv


class CSVParser:

    def get_images(self, csv_path):
        pairs = []
        with open(csv_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 1
            for row in csv_reader:
                pair = {}
                pair["image1"] = row["image1"]
                pair["image2"] = row["image2"]
                pairs.append(pair)
                line_count += 1
            return pairs

    def write_results_file(self, pairs):
        with open('results.csv', mode='w') as results:
            results_writer = csv.writer(results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            results_writer.writerow(['image1', 'image2', 'similar', 'elapsed'])
            row = 1
            for pair in pairs:
                results_writer.writerow([pair["image1"], pair["image2"], pair["similar"], pair["elapsed"]])
                row += 1