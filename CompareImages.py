import os
import sys
from classes.CSVParser import CSVParser
from classes.ComputerVision import ComputerVision


def main():
    csv_input = None
    while csv_input != "q":
        print("\n Input Path:")
        csv_input = raw_input("Please enter or copy/paste the full path of a csv file (or type 'q' to exit): \n")
        if csv_input == "q":
            sys.exit()
        if not os.path.isfile(csv_input):
            print("\n Error {}: \n File not found. \n")
        else:
            break
    print("\n Using file: " + csv_input + "\n")

    csv = CSVParser()
    images = csv.get_images(csv_input)


    print("\n Computing comparisons... \n")
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

    csv_output = None
    while csv_input != "q":
        print("\n Output Path:")
        csv_output = raw_input("Please enter or copy/paste an existing full path (or type 'q' to exit): \n")
        if csv_output == "q":
            sys.exit()
        if not os.path.isdir(csv_output):
            print("\n Error {}: \n Path not found. \n")
        else:
            break

    csv.write_results_file(result_pairs, csv_output)
    print("\n Success: \n Output has been saved to 'results.csv' ")


if __name__ == "__main__":
    main()