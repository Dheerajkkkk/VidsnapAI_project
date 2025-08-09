from flask import Flask, render_template, request
import uuid
import os

#to upload the files
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg' }

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#................


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods =["GET", "POST"])
def create():
    myid = uuid.uuid1()
    if request.method == "POST":
        print(request.files.keys())
        get_desc=request.form.get("uuid")
        get_text=request.form.get("text")
        input_files = []
        for key, value in request.files.items():
            print(key, value)

            #to upload
            file=request.files[key]
            if file:
                filename = secure_filename(file.filename)
                if(not(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'],get_desc)))):#to create the folder
                    os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'],get_desc))#to create the folder
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],get_desc, filename))
                input_files.append(file.filename)

            #capture the discrption and save it to the file
            with open(os.path.join(app.config['UPLOAD_FOLDER'],get_desc, "desc.txt") ,"w") as f:
    
                    f.write(get_text)

        for fl in input_files:
             with open(os.path.join(app.config['UPLOAD_FOLDER'],get_desc, "input.txt"), "a") as f:
                  f.write(f"file '{fl}'\nduration 1\n")
    
    

    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels = reels)

app.run(debug=True)



  