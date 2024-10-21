from flask import Flask, render_template, request,render_template_string
import subprocess

app = Flask(_name_)

# Set the path to the directory containing static files (images, CSS, etc.)
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('s1.html')

@app.route('/trigger_file1', methods=['POST'])
def trigger_file1():
    subprocess.Popen(['python', 'get_faces_from_camera_tkinter.py'])
    return '', 204

@app.route('/trigger_file2', methods=['POST'])
def trigger_file2():
    subprocess.Popen(['python', 'features_extraction_to_csv.py'])
    return '', 204

@app.route('/trigger_file3', methods=['POST'])
def trigger_file3():
    subprocess.Popen(['python', 'attendance_taker.py'])
    return '', 204

@app.route('/trigger_file4', methods=['POST'])
def trigger_file4():
    subprocess.Popen(['python', 'app.py'])
    return render_template_string('<script>window.open("http://127.0.0.1:5001", "_blank");</script>')

if _name_ == '_main_':
    app.run(debug=True, port=5000)
