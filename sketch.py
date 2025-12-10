import cv2
import numpy as np

def pencil_sketch(image_path, output_path=None):
    """
    Convert an image to pencil sketch effect
    
    Args:
        image_path: Path to input image
        output_path: Path to save output (optional)
    """
    # Read the image
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Could not read image!")
        return
    
    # Convert to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Invert the grayscale image
    inverted_img = cv2.bitwise_not(gray_img)
    
    # Apply Gaussian blur
    blurred_img = cv2.GaussianBlur(inverted_img, (21, 21), 0)
    
    # Invert the blurred image
    inverted_blurred = cv2.bitwise_not(blurred_img)
    
    # Create pencil sketch by dividing gray image by inverted blurred image
    pencil_sketch_img = cv2.divide(gray_img, inverted_blurred, scale=256.0)
    
    # Display original and sketch side by side
    cv2.imshow('Original Image', img)
    cv2.imshow('Pencil Sketch', pencil_sketch_img)
    
    # Save if output path is provided
    if output_path:
        # Add .jpg extension if not present
        if not any(output_path.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']):
            output_path += '.jpg'
        cv2.imwrite(output_path, pencil_sketch_img)
        print(f"Sketch saved to {output_path}")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return pencil_sketch_img


def pencil_sketch_colored(image_path, output_path=None):
    """
    Create a colored pencil sketch effect
    
    Args:
        image_path: Path to input image
        output_path: Path to save output (optional)
    """
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Could not read image!")
        return
    
    # Use OpenCV's built-in pencil sketch function
    sketch_gray, sketch_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
    
    # Display results
    cv2.imshow('Original Image', img)
    cv2.imshow('Grayscale Sketch', sketch_gray)
    cv2.imshow('Colored Sketch', sketch_color)
    
    if output_path:
        # Add extensions if not present
        base_path = output_path.rsplit('.', 1)[0]
        if not any(output_path.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']):
            base_path = output_path
        cv2.imwrite(base_path + '_gray.jpg', sketch_gray)
        cv2.imwrite(base_path + '_color.jpg', sketch_color)
        print(f"Sketches saved!")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return sketch_gray, sketch_color


def webcam_pencil_sketch():
    """
    Real-time pencil sketch effect using webcam
    """
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam!")
        return
    
    print("Press 'q' to quit, 's' to save screenshot")
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Invert
        inverted = cv2.bitwise_not(gray)
        
        # Blur
        blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
        
        # Invert blurred
        inverted_blurred = cv2.bitwise_not(blurred)
        
        # Create sketch
        sketch = cv2.divide(gray, inverted_blurred, scale=256.0)
        
        # Show both original and sketch
        combined = np.hstack([frame, cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)])
        cv2.imshow('Webcam Pencil Sketch (Original | Sketch)', combined)
        
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):
            break
        elif key == ord('s'):
            cv2.imwrite('sketch_screenshot.jpg', sketch)
            print("Screenshot saved as 'sketch_screenshot.jpg'")
    
    cap.release()
    cv2.destroyAllWindows()


# Main execution
if __name__ == "__main__":
    print("Pencil Sketch Effect")
    print("=" * 50)
    print("Choose an option:")
    print("1. Convert image to pencil sketch")
    print("2. Convert image to colored sketch")
    print("3. Real-time webcam pencil sketch")
    
    choice = input("\nEnter your choice (1/2/3): ")
    
    if choice == '1':
        image_path = input("Enter image path: ").strip('"').strip("'")
        save = input("Save output? (y/n): ")
        output_path = input("Enter output path (e.g., output.jpg): ").strip('"').strip("'") if save.lower() == 'y' else None
        pencil_sketch(image_path, output_path)
        
    elif choice == '2':
        image_path = input("Enter image path: ").strip('"').strip("'")
        save = input("Save output? (y/n): ")
        output_path = input("Enter output path (e.g., output.jpg): ").strip('"').strip("'") if save.lower() == 'y' else None
        pencil_sketch_colored(image_path, output_path)
        
    elif choice == '3':
        webcam_pencil_sketch()
        
    else:
        print("Invalid choice!")