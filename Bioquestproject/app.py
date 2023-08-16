from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


# Create a route for the form
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Get the uploaded file from the form
        file = request.files['image']

        # Save the file to the specified upload folder
        if file:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Save the image path to the database or perform further operations

            return redirect('/')

    return render_template('products.html')


# Create a route to display images
@app.route('/')
def index():
    # Retrieve image paths from the database or a data source
    image_paths = ['path/to/image1.jpg', 'path/to/image2.jpg', 'path/to/image3.jpg']
    return render_template('products.html ', image_paths=image_paths)


if __name__ == '__main__':
    app.run(debug=True)


