from flask import Flask, render_template

# --- App Initialization ---
app = Flask(__name__)

# --- Configuration: Web Assets Paths ---
# These are paths relative to the 'static' folder for the web application
CHOCOLATE_IMAGE_PATH = "chocolate.jpg" 
FLOWER_IMAGE_PATH = "flower.jpg"
VIDEO_LINK = "birthday_video.mp4" 

# --- Routing: Defines the sequence of pages ---

@app.route('/')
def window1_welcome():
    """Window 1: Initial Welcome and Choice."""
    return render_template('window1.html')

@app.route('/continue')
def window2_gift_message():
    """Window 2: Gift Message and Next Button."""
    return render_template('window2.html')

@app.route('/chocolates')
def window3_chocolates():
    """Window 3: Chocolates with Image."""
    return render_template('window3.html', image=CHOCOLATE_IMAGE_PATH)

@app.route('/flowers')
def window4_flowers():
    """Window 4: Flowers with Image."""
    return render_template('window4.html', image=FLOWER_IMAGE_PATH)

@app.route('/final')
def window5_final():
    """Window 5: Video playback."""
    return render_template('window5.html', video_link=VIDEO_LINK)

# --- Run the App ---
if __name__ == '__main__':
    # You will use this to test locally. For deployment, you will use a production server.
    app.run(debug=True)