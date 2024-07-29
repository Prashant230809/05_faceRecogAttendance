# import cv2

# video_capture = cv2.VideoCapture(0)
# if not video_capture.isOpened():
#     print("Unable to open the camera")
# else:
#     print("Camera is ready")
# import csv

# # Reading a CSV file
# with open('example.csv', mode='r') as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row)

# # Writing to a CSV file
# with open('output.csv', mode='w', newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['Column1', 'Column2', 'Column3'])
#     csv_writer.writerow(['Value1', 'Value2', 'Value3'])
import face_recognition
print(face_recognition.__version__)
