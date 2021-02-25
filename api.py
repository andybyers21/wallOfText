from flask import Flask, request, render_template, jsonify, session

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')


# @app.route('/background_text_process', methods=['GET', 'POST'])
# def background_text_process():
#     if request.method == 'POST':
#         text = request.form['throughput_rate_text']
#         processed_text = str(text)
#         throughput = transition_user_input(processed_text)
#         return jsonify(throughput)


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

