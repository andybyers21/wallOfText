from flask import Flask, request, render_template, Markup 
from flask_wtf.csrf import CSRFProtect

import process
import secrets

app = Flask(
      __name__,
      template_folder="templates",
      static_folder="static"
      )

# Generate random secret key for each instance of the app
secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key

csrf = CSRFProtect(app)
csrf.init_app(app)


@app.route('/')
def home():
   return render_template('home.html')


@app.route('/output', methods=['POST'])
def output():
    input_title = request.form['title']
    input_text = request.form['text']
    return render_template('output.html',
                            title_=Markup(process.title_process(input_title)),
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
    app.run(port=5000, debug=True)

