from flask import Flask, request, render_template 

app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
        )

@app.route('/')
def home():
   return render_template('home.html')


@app.route('/output', methods=['POST'])
def output():
    input_text = request.form['text']
    processed_text = input_text.upper()
    return 'You entered: {}'.format(processed_text)

# @app.route('/output')
# def output():
#     return render_template('output.html')


@app.route('/example')
def example():
    return render_template('example.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(port=1313, debug=True)

