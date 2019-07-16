import os
from CSVParser import CSVParser
from ComputerVision import ComputerVision


def main():
    basepath = os.getcwd()
    csv_input = None
    for filename in os.listdir(basepath):
        if filename.endswith('.csv'):
            csv_input = filename
            print("Using filename: " + filename)
    if csv_input == None:
        print("Error {}: \n No input csv file found. Please provide an input csv file")

    csv = CSVParser()
    images = csv.get_images(csv_input)

    computer_vision = ComputerVision()
    result_pairs = []
    for pair in images:
        if not os.path.isfile(pair["image1"]):
            print("FileNotFoundException {}: \n" + pair["image1"] + " does not exist! Please check the file path.")
            continue
        if not os.path.isfile(pair["image2"]):
            print("FileNotFoundException {}: \n" + pair["image2"] + " does not exist! Please check the file path.")
            continue
        result_pairs.append(computer_vision.find_similarity(pair))

    csv.write_results_file(result_pairs)


if __name__ == "__main__":
    main()