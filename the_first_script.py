# uploading libraries
import cv2 as cv


def robt310_project2_interpolation(input_file_name, output_file_name, scale_factor):
    # read image
    original = cv.imread(input_file_name, cv.COLOR_BGR2RGB)

    # Nearest Neighbor Interpolation (Pixel Replication)
    result = cv.resize(original, None, fx=scale_factor, fy=scale_factor, interpolation=cv.INTER_NEAREST)

    # writing new image after all operations
    cv.imwrite(output_file_name, result)


# robt310_project2_interpolation("inputs/image_1.jpg", "outputs/ex_1.jpg", 1.2)
