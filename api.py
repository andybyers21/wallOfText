from flask import Flask, request, render_template, jsonify, session

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/example')
def example():
    return render_template('example.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/join', methods=['GET', 'POST'])


def my_form_post():
    def do_something(text1, text2):
        text1 = text1.upper()
        text2 = text2.upper()
        combine = (text1 + " " + text2)
        return combine

    text1 = request.form['text1']
    text2 = request.form['text2']
    combine = do_something(text1, text2)

    result = {
        "output": combine
    }

    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)


if __name__ == '__main__':
    app.run(port=1313, debug=True)

