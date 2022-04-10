#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from keras.models import load_model
from PIL import Image #use PIL
import numpy as np
from keras.preprocessing import image


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(filename)
        file = open(filename,"r")
        model = load_model("CNN")
        test_image = image.load_img(filename, target_size = (100, 100))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        pred = model.predict(test_image)
        if pred[0][0] == 1:
          prediction = 'NORMAL'
        else:
          prediction = 'COVID'
        return(render_template("index1.html", result=str(prediction)))
    else:
        return(render_template("index1.html", result="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




