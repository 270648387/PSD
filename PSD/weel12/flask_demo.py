from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def front_page():
    return "<p> Hello, Flask! <p>"

@app.route('/username/<username>')
def learn(username):
    return f'{username} is learning Flask!'

@app.route("/<name>/<int:time>")
def time(name, time):
    return f"{name} is learning Flask! He/she wakes up at {time} every day!"

@app.route('/cal/<int:number>')
def show_square(number):
    return f"The square of {number} is {number**2}"

@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    html_form = """
    <h2>Upload an Image</h2>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="image" accept="image/*">
        <input type="submit" value="Upload">
    </form>
    {% if image_url %}
        <h3>Preview:</h3>
        <img src="{{ image_url }}" width="2000">
    {% endif %}
    """

    if request.method == 'POST':
        file = request.files['image']
        if file:
            image_path = f'static/{file.filename}'
            file.save(image_path)
            return render_template_string(html_form, image_url='/' + image_path)

    return render_template_string(html_form, image_url=None)

@app.route('/bmi/<bodyweight>/<height>')
def get_bmi(bodyweight, height):
    bodyweight = float(bodyweight)
    height = float(height)
    bmi = bodyweight/height/height
    return f'Your BMI is {bmi:.2f}'


if __name__ == '__main__':
    app.run(debug=True)