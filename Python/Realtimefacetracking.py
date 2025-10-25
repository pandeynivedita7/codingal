import cv2
import numpy as np
from datetime import datetime

class FaceTracker:
    def __init__(self):
        # Load Haar Cascade classifier for face detection
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        
        # Initialize video capture (0 for default webcam)
        self.cap = cv2.VideoCapture(0)
        
        # Set camera properties
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        # Variables for tracking
        self.face_count = 0
        self.max_faces = 0
        
    def detect_faces(self, frame):
        """Detect faces in the frame using Haar Cascade"""
        # Convert to grayscale for better detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Apply histogram equalization for better detection in varying lighting
        gray = cv2.equalizeHist(gray)
        
        # Detect faces
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,      # Scale factor for image pyramid
            minNeighbors=5,       # Minimum neighbors for detection confidence
            minSize=(30, 30),     # Minimum face size
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        return faces
    
    def draw_faces(self, frame, faces):
        """Draw rectangles around detected faces and add labels"""
        for i, (x, y, w, h) in enumerate(faces):
            # Draw rectangle around face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Add face number label
            label = f"Person {i+1}"
            cv2.putText(frame, label, (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # Draw center point
            center_x = x + w // 2
            center_y = y + h // 2
            cv2.circle(frame, (center_x, center_y), 3, (0, 0, 255), -1)
        
        return frame
    
    def add_info_panel(self, frame, face_count):
        """Add information panel with statistics"""
        # Create semi-transparent overlay
        overlay = frame.copy()
        cv2.rectangle(overlay, (10, 10), (300, 120), (0, 0, 0), -1)
        cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)
        
        # Add text information
        info_text = [
            f"Current Faces: {face_count}",
            f"Max Detected: {self.max_faces}",
            f"Time: {datetime.now().strftime('%H:%M:%S')}",
        ]
        
        y_offset = 35
        for text in info_text:
            cv2.putText(frame, text, (20, y_offset),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            y_offset += 30
        
        # Add instructions
        cv2.putText(frame, "Press 'q' to quit, 'r' to reset", 
                   (10, frame.shape[0] - 20),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        return frame
    
    def run(self):
        """Main loop for face tracking"""
        print("Starting face tracking...")
        print("Press 'q' to quit, 'r' to reset counter")
        
        while True:
            # Capture frame from webcam
            ret, frame = self.cap.read()
            
            if not ret:
                print("Failed to grab frame")
                break
            
            # Flip frame horizontally for mirror effect
            frame = cv2.flip(frame, 1)
            
            # Detect faces
            faces = self.detect_faces(frame)
            self.face_count = len(faces)
            
            # Update maximum face count
            if self.face_count > self.max_faces:
                self.max_faces = self.face_count
            
            # Draw faces and tracking info
            frame = self.draw_faces(frame, faces)
            frame = self.add_info_panel(frame, self.face_count)
            
            # Display the frame
            cv2.imshow('Face Tracking & Counting', frame)
            
            # Handle keyboard input
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('q'):
                print(f"\nSession Summary:")
                print(f"Maximum faces detected: {self.max_faces}")
                break
            elif key == ord('r'):
                self.max_faces = 0
                print("Counter reset")
        
        # Cleanup
        self.cap.release()
        cv2.destroyAllWindows()
        print("Face tracking stopped")

def main():
    """Main function to run the face tracker"""
    try:
        tracker = FaceTracker()
        tracker.run()
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you have:")
        print("1. A working webcam connected")
        print("2. OpenCV installed: pip install opencv-python")
        print("3. Proper camera permissions enabled")

if __name__ == "__main__":
    main()