# Advanced-Computer-Vision-Pipeline-Real-Time-Pencil-Sketch-Transformation
Implemented dodge-blend algorithmic rendering with Gaussian blur convolution and adaptive image inversion for photorealistic sketch synthesis.

# Pencil Sketch Transformer

Real-time image-to-sketch conversion using advanced computer vision algorithms with dodge-blend rendering and Gaussian blur convolution.

## 🎨 Overview

A Python-based computer vision pipeline that transforms photographs into photorealistic pencil sketches using adaptive image inversion, Gaussian blur convolution, and dodge-blend algorithmic rendering techniques.

## ✨ Features

- **Grayscale Sketch**: Classic pencil sketch effect using dodge-blend algorithm
- **Colored Sketch**: Artistic colored pencil rendering
- **Real-Time Processing**: Live webcam sketch transformation
- **Adaptive Rendering**: Intelligent contrast and edge preservation
- **Easy to Use**: Simple command-line interface

## 🛠️ Technology Stack

- **Python 3.x**
- **OpenCV**: Image processing and computer vision
- **NumPy**: Numerical computations

## 🚀 Installation
```bash
# Clone repository
git clone https://github.com/yourusername/pencil-sketch-transformer.git
cd pencil-sketch-transformer

# Install dependencies
pip install opencv-python numpy
```

## 📖 Usage

### Run the Program
```bash
python sketch.py
```

### Options

1. **Grayscale Sketch** - Convert image to classic pencil sketch
2. **Colored Sketch** - Create artistic colored pencil effect
3. **Webcam Mode** - Real-time sketch transformation

### Example Usage
```python
from sketch import pencil_sketch, webcam_pencil_sketch

# Transform single image
pencil_sketch('photo.jpg', 'output_sketch.jpg')

# Real-time webcam
webcam_pencil_sketch()  # Press 'q' to quit, 's' to save
```

## 🎯 How It Works

### Algorithm Pipeline
```
Input Image
    ↓
Grayscale Conversion
    ↓
Image Inversion
    ↓
Gaussian Blur (21×21 kernel)
    ↓
Dodge-Blend Division (scale=256)
    ↓
Pencil Sketch Output
```

### Core Algorithm

The dodge-blend technique mimics traditional pencil sketching:
```python
sketch = cv2.divide(gray_img, inverted_blurred, scale=256.0)
```

## 🎨 Features Breakdown

- **Gaussian Blur Convolution**: Smooths inverted image with 21×21 kernel
- **Dodge-Blend Rendering**: Division operation creates sketch effect
- **Adaptive Inversion**: Preserves edge details and contrast
- **Real-Time Capable**: Optimized for live video processing

## 📸 Controls (Webcam Mode)

- **'q'** - Quit application
- **'s'** - Save screenshot

## 📋 Requirements
```txt
opencv-python>=4.5.0
numpy>=1.19.0
```

## 🎯 Use Cases

- Digital art creation
- Photo stylization
- Educational demonstrations
- Real-time artistic filters
- Portrait sketch conversion

## 📝 License

MIT License - feel free to use and modify

## 🤝 Contributing

Contributions welcome! Feel free to submit issues and pull requests.

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Made with ❤️ using OpenCV and Python**
