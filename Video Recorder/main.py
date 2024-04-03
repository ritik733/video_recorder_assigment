import cv2

def record_video(output_file, duration=10):
    # Open the default camera (usually the first camera connected to the system)
    cap = cv2.VideoCapture(0)
    
    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))
    
    # Record video for the specified duration
    start_time = cv2.getTickCount()
    while True:
        ret, frame = cap.read()  # Capture frame-by-frame
        
        # Write the frame to the output video file
        out.write(frame)
        
        # Display the recorded video in a window
        cv2.imshow('Video Recorder', frame)
        
        # Stop recording if the specified duration has elapsed
        if cv2.waitKey(1) & 0xFF == ord('q') or \
           ((cv2.getTickCount() - start_time) / cv2.getTickFrequency()) >= duration:
            break
    
    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    output_file = 'recorded_video.avi'
    duration = 10  # in seconds
    record_video(output_file, duration)
