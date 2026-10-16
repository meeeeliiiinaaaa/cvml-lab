# Lab01_ImageFiltering

An interactive PyQt6 application for real-time and offline image filtering and edge detection using OpenCV. This is the first assignment of the Computer Vision and Machine Learning Lab course. It covers Gaussian and averaging filters, Sobel and Canny edge detection, grayscale conversion, and thresholding, with a live interface for exploring how processing parameters affect the output.

## Assignment Objectives

Implement the following functions in `filters.py`:

- `apply_gaussian_blur(...)`
- `apply_averaging_blur(...)`
- `apply_sobel_edge(...)`

`apply_canny_edge(...)` is already implemented and serves as a reference.

**Modify only `filters.py`.** Do not change `main.py`, `gui.py`, `video_thread.py`, `config.py`, or any other project file.

## Processing Pipeline

```
Input Source (Webcam or Offline Image/Video)
                    |
                  Frame
               /         \
    Blur Selection     Edge Selection
(Gaussian / Averaging)  (Sobel / Canny)
          |                  |
    Blurred View     Edge Detection View
```

## Features

- Real-time webcam processing and offline image/video input
- Three synchronized views: Original, Blurred, and Edge Detection
- Gaussian and Averaging blur modes; Sobel and Canny edge modes
- Interactive kernel, sigma, and threshold sliders with visible numeric values
- Odd-kernel handling for Gaussian filtering
- Dark-themed, responsive interface with live FPS display
- Explicit camera and file error messages
- Settings saved automatically and restored between sessions
- Reset, Restart, and Pause/Resume controls
- Keyboard shortcuts
- Safe fallbacks so an incomplete implementation does not crash the application

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/meeeeliiiinaaaa/cvml-lab01-image-filtering-main.git
   cd cvml-lab01-image-filtering
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv

   # Linux/macOS
   source venv/bin/activate

   # Windows PowerShell
   venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python main.py
   ```

## Usage

### Webcam

The application starts with the selected webcam. Use **Camera index** if your computer has more than one camera. If a camera cannot be opened, the application stays usable and shows a status message instead of crashing.

- **Webcam**: switch back to camera input
- **Pause / Resume**: freeze or continue processing
- **Restart**: reopen the current source

### Offline Images and Videos

1. Click **Browse**.
2. Select an image or video file.
3. Click **Upload** to load it into the processing pipeline.

Images remain available for interactive parameter changes. Videos play in real time and can be restarted from the beginning.

### Blur Controls

- **Gaussian Blur**: controlled by kernel size and sigma. Kernel sizes must be positive odd numbers; the interface guards against invalid even sizes while your implementation is incomplete.
- **Averaging Blur**: controlled by kernel size.

### Edge Controls

- **Sobel**: use the threshold slider in your implementation.
- **Canny**: the reference implementation uses the threshold as the lower bound and three times that value as the upper bound.

### Settings and Reset

Parameter changes apply immediately, and numeric values are shown next to every slider. The current camera and filtering parameters are saved automatically, and the status area reports the settings state. Click **Reset** to restore the default lab configuration.

## Repository Structure

```
cvml-lab01-image-filtering-main/
├── .gitignore
├── Readme.md
├── requirements.txt
├── main.py            # Application entry point
├── gui.py             # PyQt6 interface, controls, persistence, rendering
├── video_thread.py    # Capture, processing loop, FPS, error handling
├── config.py          # Shared constants and default parameters
└── filters.py         # The only file students should modify
```

## Keyboard Shortcuts

| Key   | Action           |
|-------|------------------|
| Space | Pause / Resume   |
| R     | Reset parameters |
| Q     | Quit             |
