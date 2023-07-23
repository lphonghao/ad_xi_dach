from flask import Flask, render_template, request

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for processing the form data
@app.route('/process', methods=['POST'])
def process():
    # Get the input data from the form
    input_data = request.form['input_data']

    # Call your Python function to process the input_data and get the output
    # Replace the following line with your actual Python code logic
    output_data = "Output: You entered - " + input_data

    # Pass the output to the result template
    return render_template('result.html', output=output_data)

if __name__ == '__main__':
    app.run(debug=True)
