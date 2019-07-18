import cv2
import time
import os


class ComputerVision:

    def same_image(self, image1, image2):
        image1 = cv2.imread(image1)
        image2 = cv2.imread(image2)
        if image1.shape == image2.shape:
            difference = cv2.subtract(image1, image2)
            b, g, r = cv2.split(difference)
            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                return True
        else:
            return False

    def find_similarity(self, pair, *save_image):
        start_time = time.time()

        if self.same_image(pair["image1"], pair["image2"]):
            pair["similar"] = 0

        else:
            image1 = cv2.imread(pair["image1"], cv2.IMREAD_GRAYSCALE)
            image2 = cv2.imread(pair["image2"], cv2.IMREAD_GRAYSCALE)

            # Find key points
            orb = cv2.ORB_create()
            keypoints_1, descriptors_1 = orb.detectAndCompute(image1, None)
            keypoints_2, descriptors_2 = orb.detectAndCompute(image2, None)

            # Brute Force Matching
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
            matches = bf.match(descriptors_1, descriptors_2)
            matches = sorted(matches, key=lambda x: x.distance)

            # match.distance is a float between {0:100} - lower means more similar
            good_matches = [match for match in matches if match.distance < 60]
            pair["similar"] = 1 - (float(len(good_matches)) / float(len(matches)))

            if save_image:
                image1 = cv2.imread(pair["image1"])
                image2 = cv2.imread(pair["image2"])
                matching_result = cv2.drawMatches(image1, keypoints_1, image2, keypoints_2, matches[:50], None, flags=2)
                if not os.path.isdir("./img_results"):
                    os.mkdir("img_results")
                cv2.imwrite("./img_results/similarity_" + str(pair["similar"]) + ".jpg", cv2.resize(matching_result, None, fx=0.5, fy=0.5))

        pair["elapsed"] = time.time() - start_time

        return pair
