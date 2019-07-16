# !/usr/bin/env python
import unittest
import os
import csv

from CSVParser import CSVParser
from ComputerVision import ComputerVision


def get_path():
    basepath = os.getcwd()
    dir = basepath.rsplit('/', 1)[-1]
    if dir == "tests":
        basepath += "/pics/"
    if dir == "image_comparison":
        basepath += "/tests/pics/"
    return basepath


class TestAll(unittest.TestCase):

    def test_make_csv_data(self):
        with open('test_data.csv', mode='w') as test_data:
            test_writer = csv.writer(test_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            test_writer.writerow(['image1', 'image2'])
            row = 1

            # each pair will be added to test_data.csv with the correct full paths
            pairs = ["apple_red.jpg,apple_green.jpeg", "banana1.jpg,banana2.jpeg", "bike1.jpeg,bike2.jpeg",
                     "book1.jpg,book2.jpg", "cube1.jpg,cube2.jpg", "loblaws1.png,loblaws2.jpeg",
                     "original.jpg,sunburst.jpg", "apple_red.jpg,bike2.jpeg", "banana1.jpg,cube2.jpg",
                     "book1.jpg,loblaws1.png"]

            basepath = get_path()

            for pair in pairs:
                imgs = pair.split(",")
                test_writer.writerow([basepath + imgs[0], basepath + imgs[1]])
                row += 1

    def test_get_images(self):
        csv = CSVParser()
        images = csv.get_images("test_data.csv")
        self.assertEqual(10, len(images))
        basepath = get_path()
        self.assertEqual(basepath + "apple_red.jpg", images[0]["image1"])
        self.assertEqual(basepath + "loblaws1.png", images[5]["image1"])
        self.assertEqual(basepath + "book1.jpg", images[9]["image1"])

    def test_find_similarity(self):
        csv = CSVParser()
        images = csv.get_images("test_data.csv")

        computer_vision = ComputerVision()
        result_pairs = []
        for pair in images:
            result_pairs.append(computer_vision.find_similarity(pair))

        self.assertEqual(10, len(result_pairs))
        basepath = get_path()
        self.assertEqual(basepath + "apple_red.jpg", result_pairs[0]["image1"])
        self.assertEqual(basepath + "loblaws1.png", images[5]["image1"])
        self.assertEqual(basepath + "book1.jpg", images[9]["image1"])



    def test_write_results_file(self):
        csv = CSVParser()
        images = csv.get_images("test_data.csv")

        computer_vision = ComputerVision()
        result_pairs = []
        for pair in images:
            result_pairs.append(computer_vision.find_similarity(pair))

        csv.write_results_file(result_pairs)


if __name__ == '__main__':
    unittest.main()