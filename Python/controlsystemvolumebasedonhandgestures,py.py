import cv2
import pycaw as pc # Corrected import for clarity.
import mediapipe as mp
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7) # Added confidence parameters

# Initialize pycaw for volume control
# Get default audio device
devices = pc.AudioUtilities.Get
# Get the master volume control interface
interface = devices.GetSpeakers().Activate(
    pc.IAudioEndpointVolume._iid_, pc.CLSCTX_ALL, None)
volume = interface.QueryInterface(pc.IAudioEndpointVolume)

# Get current volume range
vol_range = volume.GetVolumeRange() # Returns (min_decibels, max_decibels, increment)
min_vol = vol_range[0]
max_vol = vol_range[1]

# Initialize OpenCV camera
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit() # Exit if camera can't be opened

# Variables for smoothing volume changes (optional, but recommended)
prev_vol_percentage = 0
smoothing_factor = 0.8 # Adjust as needed (0.0 to 1.0)

print("Starting hand gesture volume control. Press 'q' to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break # Exit loop if frame can't be read

    # Flip the frame horizontally for a more intuitive view (optional)
    frame = cv2.flip(frame, 1)

    # Convert the BGR frame to RGB for MediaPipe
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image with MediaPipe Hands
    results = hands.process(img_rgb)

    h, w, c = frame.shape # Get frame dimensions

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks on the frame
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get coordinates of thumb tip (4) and index finger tip (8)
            x1, y1 = int(hand_landmarks.landmark[4].x * w), int(hand_landmarks.landmark[4].y * h)
            x2, y2 = int(hand_landmarks.landmark[8].x * w), int(hand_landmarks.landmark[8].y * h)

            # Draw circles at thumb and index finger tips
            cv2.circle(frame, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
            cv2.circle(frame, (x2, y2), 10, (255, 0, 255), cv2.FILLED)

            # Draw a line between thumb and index finger tips
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # Calculate the distance between thumb and index finger tips
            length = math.hypot(x2 - x1, y2 - y1)

            # Map the distance to the volume range
            # Adjust these min_dist and max_dist values based on your hand size and comfort
            min_dist = 30  # Minimum distance for volume (fingers close)
            max_dist = 200 # Maximum distance for volume (fingers far apart)

            # Clamp the length to the defined range to avoid out-of-bounds mapping
            clamped_length = max(min_dist, min(length, max_dist))

            # Linear interpolation to map distance to a 0-100 percentage
            vol_percentage = int(math.interp(clamped_length, [min_dist, max_dist], [0, 100]))

            # Apply smoothing to the volume change
            current_vol_percentage = (prev_vol_percentage * smoothing_factor) + \
                                      (vol_percentage * (1 - smoothing_factor))
            prev_vol_percentage = current_vol_percentage

            # Map the percentage to the actual decibel range for pycaw
            # pycaw expects a value between min_vol and max_vol (decibels)
            target_vol_db = math.interp(current_vol_percentage, [0, 100], [min_vol, max_vol])

            # Set the system volume
            volume.SetMasterVolumeLevel(target_vol_db, None)

            # Display volume percentage on the frame
            cv2.putText(frame, f'Vol: {int(current_vol_percentage)}%', (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Visualize the volume bar (optional)
            bar_height = int(math.interp(current_vol_percentage, [0, 100], [h // 2, 50]))
            cv2.rectangle(frame, (w - 85, h // 2), (w - 50, bar_height), (0, 255, 0), cv2.FILLED)
            cv2.rectangle(frame, (w - 85, h // 2), (w - 50, 50), (0, 0, 255), 2) # Outline

    # Display the frame
    cv2.imshow('Hand Volume Control', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
hands.close() # Close MediaPipe hands instance