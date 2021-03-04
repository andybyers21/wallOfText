from flask import Flask, request, render_template, Markup 

import process

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
    return render_template('output.html',
                            string_=Markup(process.text_process(input_text))
                            )


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
    app.run(port=1111, debug=True)

