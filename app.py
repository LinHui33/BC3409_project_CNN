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
def CNN():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save("static/" + filename)
        file = open("static/" + filename,"r")
        model = load_model("CNN_ResNet50")
        test_image = image.load_img("static/" + filename, target_size = (100, 100))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        pred = model.predict(test_image)
        if pred[0][0] == 1:
            s = "Covid"
        else:
            s = "Normal"
        return(render_template("CNN.html", result=str(s)))
    else:
        return(render_template("CNN.html", result="pending"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




