#   python resolver.py --image image/ex1.jpg
import argparse

'''
Function : cv2.cornerHarris(image,blocksize,ksize,k)
Parameters are as follows :
1. image : the source image in which we wish to find the corners (grayscale)
2. blocksize : size of the neighborhood in which we compare the gradient 
3. ksize : aperture parameter for the Sobel() Operator (used for finding Ix and Iy)
4. k : Harris detector free parameter (used in the calculation of R)
'''

def harris_corners(image):
    
    #Converting the image to grayscale
    gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    #Conversion to float is a prerequisite for the algorithm
    gray_img = np.float32(gray_img)
    
    # 3 is the size of the neighborhood considered, aperture parameter = 3
    # k = 0.04 used to calculate the window score (R)
    corners_img = cv2.cornerHarris(gray_img,3,3,0.04)
    
    #Marking the corners in Green
    image[corners_img>0.001*corners_img.max()] = [0,255,0]

    return image


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the input image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
harris = harris_corners(image)
cv2.imshow("harris", harris)
cv2.waitKey(0)
