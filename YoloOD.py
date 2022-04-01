import cv2

cap= cv2.VideoCapture(1)
net = cv2.dnn.readNetFromDarknet('yolo/yolov3.cfg', 'yolo/yolov3.weights')
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
classes = open('yolo/coco.names').read().strip().split('\n')
width, height = 1280, 720
cap.set(3,416)
cap.set(4, 416)


def toBlob(im):
    blob = cv2.dnn.blobFromImage(im, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    return blob


while True:


    ret, img = cap.read()
    if ret:
        img=cv2.flip(img,1)
        
        input = toBlob(img)
        net.setInput(input)
        outputs=net.forward(ln)
        r = input[0, 0, :, :]

        for out in outputs:
            print(out.shape)

        cv2.imshow('test',r)
        




        if cv2.waitKey(1) & 0xFF==ord('q'):
            cv2.destroyAllWindows()
            cap.release()
            print('debugg')
            break



