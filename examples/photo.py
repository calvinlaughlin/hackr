import curses
import cv2
import numpy as np

def adjust_brightness_contrast(image, brightness=30, contrast=1.5):
    # Convert image to float, scale, adjust contrast and brightness, and clip values
    image = np.asfarray(image)
    image = image * contrast + brightness
    image = np.clip(image, 0, 255)
    return image.astype(np.uint8)

def take_and_show_photo():
    # Initialize the camera
    cap = cv2.VideoCapture(0)  # 0 is typically the default camera
    if not cap.isOpened():
        return False
    
    # Take a photo
    ret, frame = cap.read()
    if ret:
        # Adjust brightness and contrast
        frame = adjust_brightness_contrast(frame)

        cv2.imshow("Photo", frame)  # Display the frame in a window
        cv2.waitKey(3000)  # Wait for 3000 ms before closing window automatically
        cv2.destroyAllWindows()  # Close the window
    cap.release()
    return ret

def main(screen):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    screen.keypad(True)  # Enable keypad mode
    screen.addstr("Press 'p' to take a photo, 'q' to quit\n")
    screen.refresh()
    
    while True:
        key = screen.getch()
        if key == ord('q'):
            break
        elif key == ord('p'):
            if take_and_show_photo():
                screen.addstr("Photo taken and displayed!\n")
            else:
                screen.addstr("Failed to take photo. Check your camera.\n")
            screen.refresh()

curses.wrapper(main)
