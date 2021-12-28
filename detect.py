# OpenCV Facial Detection Program
# Andrew Flores
# Colorado State University
# Last Modified: 12.28.21

import cv2

# BEGIN LIVE CAPTURE BLOCK
# Live capture face and eye detection
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
upper_body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # upperbody = upper_body_cascade.detectMultiScale(gray, 1.1, 3)
    # for (ux, uy, uw, uh) in upperbody:
    #     cv2.rectangle(frame, (ux, uy), (ux + uw, uy + uh), (255, 0, 255), 2)

    faces = face_cascade.detectMultiScale(gray, 1.4, 3)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.25, 4)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)
        # smile = smile_cascade.detectMultiScale(roi_gray, 1.3, 10)
        # for (sx, sy, sw, sh) in smile:
        #     cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)

    width = int(cap.get(3))
    height = int(cap.get(4))

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
# END LIVE CAPTURE BLOCK

# # BEGIN PHOTO BLOCK
# # Photo face and eye detection
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
# smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
# full_body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# filepath = 'game_boys.jpg'
# frame = cv2.imread(filepath)

# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# faces = face_cascade.detectMultiScale(gray, 1.07, 8)

# for (x, y, w, h) in faces:
#     cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
#     roi_gray = gray[y:y+h, x:x+w]
#     roi_color = frame[y:y+h, x:x+w]
#     eyes = eye_cascade.detectMultiScale(roi_gray, 1.17, 8)
#     for (ex, ey, ew, eh) in eyes:
#         cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)
#     smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 8)
#     for (sx, sy, sw, sh) in smile:
#         cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 5)


# cv2.imshow('frame', frame)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # END PHOTO BLOCK