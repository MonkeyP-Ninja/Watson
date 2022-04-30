import pixellib
from pixellib.torchbackend.instance import instanceSegmentation
import pycocotools

ins = instanceSegmentation()
ins.load_model("pointrend_resnet50.pkl")
ins.segmentImage("img.jpg", show_bboxes=True, output_image_name="output_image.jpg")
