from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <div>
        <div><a href="https://google.com">Search in Google</a></div>
        <div>
          <input id="imgInput" type="text" placeholder="Image URL"/>
        </div>
        <div>
          <img id="preview" src="https://picsum.photos/200" width="200" height="200"/>
        </div>
        <script>
          const input = document.getElementById('imgInput');
          const img = document.getElementById('preview');
          input.addEventListener('input', () => {
            const url = input.value.trim();
            img.src = url
          });
        </script>
    </div>
    """


if __name__ == "__main__":
    app.run(debug=True)