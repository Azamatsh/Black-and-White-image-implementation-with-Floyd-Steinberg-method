# uploading libraries
import cv2 as cv
from skimage.exposure import match_histograms


def robt310_project2_histogram_match(input_file_name1, input_file_name2):
    # read images
    file_1 = cv.imread(input_file_name1, 0)
    file_2 = cv.imread(input_file_name2, 0)

    matched = match_histograms(file_1, file_2, channel_axis=True)

    # writing new image of resulted matched histogram
    cv.imwrite("outputs/ex_3.jpg", matched)


# robt310_project2_histogram_match("inputs/image_3_1.jpeg", "inputs/image_3_2.jpeg")
