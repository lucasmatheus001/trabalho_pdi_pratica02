import sys
import cv2

def main(argv):

    ddepth = cv2.CV_16S
    kernel_size = 3

    src = cv2.imread('lena_gray.bmp',0)

    # dst = cv2.Laplacian(src, ddepth, kernel_size)
    dst = cv2.Laplacian(src, ddepth, ksize=kernel_size)

    abs_dst = cv2.convertScaleAbs(dst)

    window_name = "Laplace Demo"
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(window_name, abs_dst)

    cv2.waitKey(0)
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])