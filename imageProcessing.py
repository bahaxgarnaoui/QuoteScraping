import cv2
import numpy as np
import requests

def download_image(url):
    response = requests.get(url)
    response.raise_for_status()
    image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    return image


def has_gray_square_background(image, gray_threshold=200, area_threshold=800):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, gray_threshold, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    gray_squares = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > area_threshold:
            approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
            if len(approx) == 4:
                gray_squares += 1
    return gray_squares > 0

def image_processing(url):
    try:
        image = download_image(url)
        if image is not None and not has_gray_square_background(image):
            print("The image meets the requirements.")
            return True
        else:
            print("The image does not meet the requirements.")
            return False
    except :
        print("Failed to download the image.")
        return False

image_processing("https://th.bing.com/th/id/OIP.r-4nPWdl2YmDv8i4sYV7YgHaHa?w=178&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7")
image_processing("https://th.bing.com/th/id/OIP.KndE1p0tLceL8VuG5D2TGgHaHr?w=172&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7")