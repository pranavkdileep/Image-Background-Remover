from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__, template_folder='template')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded image file
        file = request.files['image'].read()

        # Check that the uploaded file is a valid image file
        try:
            image = Image.open(io.BytesIO(file))
        except:
            return render_template('index.html', error='Invalid image file')

        # Remove the background from the image using rembg
        with open('input.png', 'wb') as f:
            f.write(file)
        with open('output.png', 'wb') as f:
            f.write(remove(file))

        # Return the result to the user
        return render_template('index.html', result='output.png')

    # If the request method is GET, render the upload form
    return render_template('index.html')

@app.route('/download')
def download():
    # Download the resulting image file
    return send_file('output.png', as_attachment=True)
    

    
if __name__ == '__main__':
    app.run()
