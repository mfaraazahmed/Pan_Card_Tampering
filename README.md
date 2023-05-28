# PAN Card Tampering Web App

This web application is designed to detect tampering in PAN cards using image processing techniques. It compares the uploaded PAN card image with an original reference image to identify any modifications or alterations.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/pan-card-tampering-web-app.git
2. Navigate to the project directory:
    ```bash
    cd pan-card-tampering-web-app
3. Create a virtual environment (optional but recommended):
    ```
    python3 -m venv env
    source env/bin/activate 
4. Install the required dependencies:
    ```
    pip install -r requirements.txt

## Usage

1. Start the Flask development server:
    ```
    export FLASK_APP=hello.py
    python -m flask run

2. Open your web browser and access the web app at http://localhost:5000.

3. Upload a PAN card image using the provided form.

4. The app will process the uploaded image and compare it with the original image.

5. The app will display the uploaded image, the difference image, the thresholded image, and the prediction result indicating the percentage of correctness.

## File

- requirements.txt: Contains the list of required dependencies for the project.

- app/views.py: Contains the main Flask application code including routes and image processing logic.

## Dependencies

The following dependencies are required to run the project:

- blinker==1.6.2
- click==8.1.3
- Flask==2.3.2
- gunicorn==20.1.0
- imageio==2.29.0
- importlib-metadata==6.6.0
- imutils==0.5.4
- itsdangerous==2.1.2
- Jinja2==3.1.2
- lazy_loader==0.2
- MarkupSafe==2.1.2
- networkx==3.1
- numpy==1.24.3
- opencv-python==4.7.0.72
- packaging==23.1
- Pillow==9.5.0
- PyWavelets==1.4.1
- scikit-image==0.20.0
- scipy==1.9.1
- tifffile==2023.4.12
- Werkzeug==2.3.4
- zipp==3.15.0

Make sure to install these dependencies before running the application.