# uploading libraries
import cv2 as cv
import numpy as np
import skimage.morphology as morp
from skimage.filters import rank


def robt310_project2_histogram_equalize(input_file_name):
    # read image
    original = cv.imread(input_file_name, 0)

    # Histogram Equalization
    histogram_equalization = cv.equalizeHist(original)

    # saving resulted histogram equalization image
    cv.imwrite("outputs/ex_2_hist.jpg", histogram_equalization)

    # local histogram equalization
    local_histogram_equalization = rank.equalize(original, morp.disk(40))

    # saving resulted local histogram equalization image
    cv.imwrite("outputs/ex_2_local_hist.jpg", local_histogram_equalization)

    # writing new image with previous versions for comparison
    # done for convenience
    cv.imwrite("outputs/ex_2_compare.jpg",  np.hstack((original, histogram_equalization, local_histogram_equalization)))


# secret file was renamed to image_2
# robt310_project2_histogram_equalize("inputs/image_2.png")
