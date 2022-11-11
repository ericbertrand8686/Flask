from flask import Flask, render_template, request, redirect, flash, url_for
import urllib.request
from werkzeug.utils import secure_filename

import os
import base64

from keras.models import load_model
from keras.utils.image_utils import load_img
from keras.utils.image_utils import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions

import tensorflow

app = Flask(__name__)

model = load_model('Diagnostic_Rétine/retinal-oct_20e_le3e-4.h5')

def getPrediction(filename):
    return 'toto'
    # image = load_img('uploads/'+filename, target_size=(224, 224))
    # image = img_to_array(image)
    # image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # image = preprocess_input(image)
    # yhat = model.predict(image)
    # label = decode_predictions(yhat)
    # label = label[0][0]
    # print('%s (%.2f%%)' % (label[1], label[2]*100))
    # return label[1], label[2]*100


@app.route('/')
def hello():
    return render_template("index.html", message="Bienvenue sur la page d'accueil !")


@app.route('/', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        if 'fichiers' not in request.files:
            return render_template("index.html", message="Pas de fichiers dans le POST !")
        file = request.files.getlist('fichiers')

        return render_template("predict.html", message="Prédiction", prediction_text = getPrediction(0), my_img = base64.b64encode(file[0].read()))
    #     if file.filename == '':
    #         flash('No file selected for uploading')
    #         return redirect(request.url)
    #     if file:
    #         filename = secure_filename(file.filename)
    #         file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    #         getPrediction(filename)
    #         label, acc = getPrediction(filename)
    #         flash(label)
    #         flash(acc)
    #         flash(filename)
    #         return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
