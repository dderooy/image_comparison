import os
from CSVParser import CSVParser
from ComputerVision import ComputerVision


def main():
    if not os.path.isfile('./input_data.csv'):
        print("\n Error {}: \n No input_data.csv file found. Please provide the input file with the exact name 'input_data.csv' \n")

    csv = CSVParser()
    images = csv.get_images("input_data.csv")

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