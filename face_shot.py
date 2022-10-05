import cv2

#Input your name
name = input("Nhập tên của bạn: ")

cam = cv2.VideoCapture(0)
cv2.nameWindow("Vui lòng nhấn space để chụp ảnh", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Vui lòng nhấn space để tiếp tục", 500, 300)

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Nhấn space để chụp", frame)

    k = cv2.waitkey(1)
    if k % 256 == 27:
        print("Nhấn Esc để kết thúc")
        break
    elif k % 256 == 32:
        img_name = "dataset/" + name + "/image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
