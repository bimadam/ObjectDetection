from imageai.Detection import ObjectDetection

recognizer = ObjectDetection()

path_input = "./Input/images.jpg"
path_output = "./Output/newimage.jpg"

recognizer.setModelTypeAsTinyYOLOv3()
recognizer.setModelPath("tiny-yolov3.pt")
recognizer.loadModel()

recognition = recognizer.detectObjectsFromImage(
    input_image = path_input,
    output_image_path = path_output
)

for eachItem in recognition:
    print(eachItem["name"] , " : ", eachItem["percentage_probability"])