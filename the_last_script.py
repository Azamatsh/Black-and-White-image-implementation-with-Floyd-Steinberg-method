# uploading libraries
import cv2 as cv
import numpy as np


def robt310_project2_dither(input_file_name, output_file_name, part):
    # read image
    pixel = cv.imread(input_file_name)

    # change image to gray colors
    pixel = cv.cvtColor(pixel, cv.COLOR_BGR2GRAY)

    # writing gray image to jpg file
    cv.imwrite("outputs/ex_4_gray.jpg", pixel)

    # all pixels were divided to 255 as far as maximum intensity was 255
    pixel = np.array(pixel) / 255

    # for the convenience height and width
    # was changed to top_to_bottom and left_to_right
    top_to_bottom, left_to_right = pixel.shape

    # rewritten and adopted code from the document
    # almost all code was kept the same with minor changes
    for x in range(top_to_bottom - 1):
        for y in range(left_to_right - 1):
            oldpixel = pixel[x][y]
            newpixel = np.round(oldpixel)
            pixel[x][y] = newpixel
            quant_error = oldpixel - newpixel
            pixel[x + 1][y] = pixel[x + 1][y] + quant_error * 7 / 16
            pixel[x - 1][y + 1] = pixel[x - 1][y + 1] + quant_error * 3 / 16
            pixel[x][y + 1] = pixel[x][y + 1] + quant_error * 5 / 16
            pixel[x + 1][y + 1] = pixel[x + 1][y + 1] + quant_error * 1 / 16

    # multiplication to maximum intensity back
    # also division to maximum value of matrix due to the fact that
    # some cells may exceed 1, for example 1.3
    pixel *= 255 / max([max(x) for x in pixel])

    # writing new image after all operations
    cv.imwrite(output_file_name, pixel)


# running function with input file name and output file name
robt310_project2_dither("inputs/image_4.jpg", "outputs/ex_4.jpg", 0)
