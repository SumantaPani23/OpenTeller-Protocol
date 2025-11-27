import cv2
from ultralytics import YOLO
from loguru import logger

class Sentinel:
    """
    The Vision Security Unit. 
    Detects 'Shoulder Surfing' (more than 1 person in frame).
    """
    
    def __init__(self):
        # Load a lightweight model (Nano version) for speed
        logger.info("Initializing Sentinel Vision System...")
        self.model = YOLO('yolov8n.pt') 

    def analyze_frame(self, frame):
        """
        Takes a camera frame, counts people.
        Returns: (is_safe: bool, person_count: int)
        """
        results = self.model(frame, verbose=False)
        
        # Count objects classified as 'person' (class ID 0)
        person_count = 0
        for r in results:
            for box in r.boxes:
                if int(box.cls) == 0:  # 0 is the ID for 'person' in COCO dataset
                    person_count += 1
        
        # Rule: If > 1 person seen, it is a security risk.
        is_safe = person_count <= 1
        
        return is_safe, person_count