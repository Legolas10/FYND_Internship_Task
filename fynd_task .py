# -*- coding: utf-8 -*-
"""fynd_task.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17OM1g1PjPWVWTJdTjjjuEIzSURrQdvPJ
"""

from google.colab import drive

drive.mount('/content/drive',force_remount=True)

cd /content/drive/My Drive/Lego_Colab/Fynd_ML_Hackathon

import os
os.makedirs("dataset1/train/", exist_ok=True)
os.makedirs("dataset1/test/", exist_ok=True)

import pandas as pd
import numpy as np
import seaborn as sns
import os

data=pd.read_csv('data.csv')
x_train=pd.read_csv('train_features.csv')
x_test=pd.read_csv('test_features.csv')
#data is ready...pass it onto pre-tr mlp
x_tr=x_train
x_te=x_test


classes=list(data['class'].unique())

#MISSING VALUES:
data.isnull().sum()

d=data

data=data.astype(str)
data.dtypes

y=data['class'].copy()
y.value_counts()
sns.countplot(y)

all_nan_url=[]
for i in range(0,data.shape[0]):
    urls=list(data.iloc[i])
    count=0
    for j in range(1,len(urls)):
        if(urls[j]=="nan"):
            all_nan_url.append(i)
#FORTUNATELY THERE IS NO DATA WITH ALL NAN VALUES..
print(all_nan_url)

#so i fill the nan values with any other available view url
for i in range(data.shape[0]):
    urls=list(data.iloc[i])
    for j in range(1,6):
        if(urls[j]!="nan"):
            curr_url=urls[j]
        elif(urls[j]=="nan"):
            urls[j]=curr_url
    data.iloc[i]=urls        

data.isnull().sum()
#no missing data

y=data['class'].copy()
y.value_counts()
sns.countplot(y)
#DATA IS NOT SO IMBALANCED....so assuming that data is not imbalanced

import urllib.request as urlr  


cl1_len=list(data[data['class']=='zipper'].index-100)
cl2_len=list(data[data['class']=='backstrap'].index-100)
cl3_len=list(data[data['class']=='slip_on'].index-100)
cl4_len=list(data[data['class']=='lace_up'].index-100)
cl5_len=list(data[data['class']=='buckle'].index-100)
cl6_len=list(data[data['class']=='hook&look'].index-100)

for i in cl1_len:
    ur=list(data.iloc[i])
    tar=ur[-1]
    ur=ur[1:-1]
    count=0
    for j in ur:
        count+=1
        img_name=j.split("/",6)[-1]+"_"+j.split("/",6)[-2]
        file_name=tar
        fin="train/"+file_name+"/"+img_name+str(count)
        img=urlr.urlretrieve(j,fin)
    

for i in cl2_len:
    ur=list(data.iloc[i])
    tar=ur[-1]
    ur=ur[1:-1]
    count=0
    for j in ur:
        count+=1
        img_name=j.split("/",6)[-1]+"_"+j.split("/",6)[-2]
        file_name=tar
        fin="train/"+file_name+"/"+img_name+str(count)
        img=urlr.urlretrieve(j,fin)
    

for i in cl3_len:
    ur=list(data.iloc[i])
    tar=ur[-1]
    ur=ur[1:-1]
    count=0
    for j in ur:
        count+=1
        img_name=j.split("/",6)[-1]+"_"+j.split("/",6)[-2]
        file_name=tar
        fin="train/"+file_name+"/"+img_name+str(count)
        img=urlr.urlretrieve(j,fin)
    

for i in cl4_len:
    ur=list(data.iloc[i])
    tar=ur[-1]
    ur=ur[1:-1]
    count=0
    for j in ur:
        count+=1
        img_name=j.split("/",6)[-1]+"_"+j.split("/",6)[-2]
        file_name=tar
        fin="train/"+file_name+"/"+img_name+str(count)
        img=urlr.urlretrieve(j,fin)
    

for i in cl5_len:
    ur=list(data.iloc[i])
    tar=ur[-1]
    ur=ur[1:-1]
    count=0
    for j in ur:
        count+=1
        img_name=j.split("/",6)[-1]+"_"+j.split("/",6)[-2]
        file_name=tar
        fin="train/"+file_name+"/"+img_name+str(count)
        img=urlr.urlretrieve(j,fin)
    

for i in cl6_len:
    ur=list(data.iloc[i])
    tar=ur[-1]
    ur=ur[1:-1]
    count=0
    for j in ur:
        count+=1
        img_name=j.split("/",6)[-1]+"_"+j.split("/",6)[-2]
        file_name=tar
        fin="train/"+file_name+"/"+img_name+str(count)
        img=urlr.urlretrieve(j,fin)
                    
#250 images in total

#create train and test data        
#25 % test and 70 % train        

#SPLITIING LAST 20 ITEMS FOR TEST DATA..
for i in range(480,500):
    ur=list(data.iloc[i])
    tar=ur[-1]
    ur=ur[1:-1]
    count=0
    for j in ur:
        count+=1
        img_name=j.split("/",6)[-1]+"_"+j.split("/",6)[-2]
        file_name=tar
        fin="test/"+file_name+"/"+img_name+str(count)
        img=urlr.urlretrieve(j,fin)
                    
        

for i in range(1240,1260):
    ur=list(data.iloc[i])
    tar=ur[-1]
    ur=ur[1:-1]
    count=0
    for j in ur:
        count+=1
        img_name=j.split("/",6)[-1]+"_"+j.split("/",6)[-2]
        file_name=tar
        fin="test/"+file_name+"/"+img_name+str(count)
        img=urlr.urlretrieve(j,fin)
                           
len_total=data.shape[0]/3

for i in range(815,835):
    ur=list(data.iloc[i])
    tar=ur[-1]
    ur=ur[1:-1]
    count=0
    for j in ur:
        count+=1
        img_name=j.split("/",6)[-1]+"_"+j.split("/",6)[-2]
        file_name=tar
        fin="test/"+file_name+"/"+img_name+str(count)
        img=urlr.urlretrieve(j,fin)
                   


for i in range(1692,1712):
    ur=list(data.iloc[i])
    tar=ur[-1]
    ur=ur[1:-1]
    count=0
    for j in ur:
        count+=1
        img_name=j.split("/",6)[-1]+"_"+j.split("/",6)[-2]
        file_name=tar
        fin="test/"+file_name+"/"+img_name+str(count)
        img=urlr.urlretrieve(j,fin)
                   


for i in range(1832,1852):
    ur=list(data.iloc[i])
    tar=ur[-1]
    ur=ur[1:-1]
    count=0
    for j in ur:
        count+=1
        img_name=j.split("/",6)[-1]+"_"+j.split("/",6)[-2]
        file_name=tar
        fin="test/"+file_name+"/"+img_name+str(count)
        img=urlr.urlretrieve(j,fin)
                          
        

for i in range(2136,2156):
    ur=list(data.iloc[i])
    tar=ur[-1]
    ur=ur[1:-1]
    count=0
    for j in ur:
        count+=1
        img_name=j.split("/",6)[-1]+"_"+j.split("/",6)[-2]
        file_name=tar
        fin="test/"+file_name+"/"+img_name+str(count)
        img=urlr.urlretrieve(j,fin)

#ALREADY RAN AND STORED IN LOCAL FOLDER...AFTER SCRAPING ALL URL'S FOR DATA

#NOW THAT THE DATA IS READY...WE DEPLOY A CNN....OR USE AN AUTOENCODER....
import keras
from keras.models import Sequential
from keras.layers import Dense,Conv2D,MaxPooling2D
import keras.regularizers
from keras import regularizers
from keras.layers import Flatten,Dropout

#METHOD 3: USE TRANSFER LEARNING..

from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input,decode_predictions
from keras.applications.vgg16 import VGG16
train_path="dataset/train"
test_path="dataset/test"

from scipy.misc import imresize

x_train=[]
y_train=[]
for j in range(1,286):
    ti=image.load_img(train_path+"/zipper/"+"file-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_train.append(ti)
    y_train.append('zipper')
    
for j in range(1,251):
    ti=image.load_img(train_path+"/backstrap/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_train.append(ti)
    y_train.append('backstrap')
    
for j in range(1,251):
    ti=image.load_img(train_path+"/slip_on/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_train.append(ti)
    y_train.append('slip_on')

for j in range(1,251):
    ti=image.load_img(train_path+"/lace_up/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_train.append(ti)
    y_train.append('lace_up')
    
for j in range(1,251):
    ti=image.load_img(train_path+"/buckle/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_train.append(ti)
    y_train.append('buckle')

for j in range(1,251):
    ti=image.load_img(train_path+"/hook&look/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_train.append(ti)
    y_train.append('hook&look')

x_test=[]
y_test=[]            

for j in range(1,101):
    ti=image.load_img(test_path+"/zipper/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_test.append(ti)
    y_test.append('zipper')

for j in range(1,101):
    ti=image.load_img(test_path+"/backstrap/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_test.append(ti)
    y_test.append('backstrap')

           
for j in range(1,101):
    ti=image.load_img(test_path+"/slip_on/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_test.append(ti)
    y_test.append('slip_on')
    
for j in range(1,101):
    ti=image.load_img(test_path+"/lace_up/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_test.append(ti)
    y_test.append('lace_up')


for j in range(1,101):
    ti=image.load_img(test_path+"/buckle/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_test.append(ti)
    y_test.append('buckle')


for j in range(1,101):
    ti=image.load_img(test_path+"/hook&look/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_test.append(ti)
    y_test.append('hook&look')

#2nd time...data augmentation
#METHOD 3: USE TRANSFER LEARNING..

from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input,decode_predictions
from keras.applications.vgg16 import VGG16
train_path="dataset/train"
test_path="dataset/test"

from scipy.misc import imresize

for j in range(1,286):
    ti=image.load_img(train_path+"/zipper/"+"file-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_train.append(ti)
    y_train.append('zipper')
    
for j in range(1,251):
    ti=image.load_img(train_path+"/backstrap/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_train.append(ti)
    y_train.append('backstrap')
    
for j in range(1,251):
    ti=image.load_img(train_path+"/slip_on/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_train.append(ti)
    y_train.append('slip_on')

for j in range(1,251):
    ti=image.load_img(train_path+"/lace_up/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_train.append(ti)
    y_train.append('lace_up')
    
for j in range(1,251):
    ti=image.load_img(train_path+"/buckle/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_train.append(ti)
    y_train.append('buckle')

for j in range(1,251):
    ti=image.load_img(train_path+"/hook&look/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_train.append(ti)
    y_train.append('hook&look')

for j in range(1,101):
    ti=image.load_img(test_path+"/zipper/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_test.append(ti)
    y_test.append('zipper')

for j in range(1,101):
    ti=image.load_img(test_path+"/backstrap/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_test.append(ti)
    y_test.append('backstrap')

           
for j in range(1,101):
    ti=image.load_img(test_path+"/slip_on/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_test.append(ti)
    y_test.append('slip_on')
    
for j in range(1,101):
    ti=image.load_img(test_path+"/lace_up/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_test.append(ti)
    y_test.append('lace_up')


for j in range(1,101):
    ti=image.load_img(test_path+"/buckle/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_test.append(ti)
    y_test.append('buckle')


for j in range(1,101):
    ti=image.load_img(test_path+"/hook&look/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_test.append(ti)
    y_test.append('hook&look')

    
for j in range(1,286):
    ti=image.load_img(train_path+"/zipper/"+"file-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_train.append(ti)
    y_train.append('zipper')
    
for j in range(1,251):
    ti=image.load_img(train_path+"/backstrap/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_train.append(ti)
    y_train.append('backstrap')
    
for j in range(1,251):
    ti=image.load_img(train_path+"/slip_on/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_train.append(ti)
    y_train.append('slip_on')

for j in range(1,251):
    ti=image.load_img(train_path+"/lace_up/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_train.append(ti)
    y_train.append('lace_up')
    
for j in range(1,251):
    ti=image.load_img(train_path+"/buckle/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_train.append(ti)
    y_train.append('buckle')

for j in range(1,251):
    ti=image.load_img(train_path+"/hook&look/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_train.append(ti)
    y_train.append('hook&look')

for j in range(1,101):
    ti=image.load_img(test_path+"/zipper/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_test.append(ti)
    y_test.append('zipper')

for j in range(1,101):
    ti=image.load_img(test_path+"/backstrap/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_test.append(ti)
    y_test.append('backstrap')

           
for j in range(1,101):
    ti=image.load_img(test_path+"/slip_on/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_test.append(ti)
    y_test.append('slip_on')
    
for j in range(1,101):
    ti=image.load_img(test_path+"/lace_up/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_test.append(ti)
    y_test.append('lace_up')


for j in range(1,101):
    ti=image.load_img(test_path+"/buckle/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_test.append(ti)
    y_test.append('buckle')


for j in range(1,101):
    ti=image.load_img(test_path+"/hook&look/"+"image-"+str(j)+".jpg",target_size=(224,224))
    ti=image.img_to_array(ti)
    x_test.append(ti)
    y_test.append('hook&look')

import numpy as np
x_train=np.array(x_train)
y_train=np.array(y_train)
x_test=np.array(x_test)
y_test=np.array(y_test)

x_train=preprocess_input(x_train)
x_test= preprocess_input(x_test)

x_train.shape
x_test.shape

#now extract features from train dataset using the vgg per-trained model
model = VGG16(weights='imagenet', include_top=False)

features_train=model.predict(x_train)

features_test=model.predict(x_test)

train_x=features_train.reshape(features_train.shape[0],25088)
test_x=features_test.reshape(features_test.shape[0],(features_test.shape[1]*features_test.shape[2]*features_test.shape[3]))
fttt=test_x
fttr=train_x

train_features=pd.DataFrame(fttr)
test_features=pd.DataFrame(fttt)
train_features.to_csv('train_features.csv',index=False)
test_features.to_csv('test_features.csv',index=False)

#data is ready...pass it onto pre-tr mlp
# x_tr=x_train
# x_te=x_test
x_train=x_tr
x_test=x_te

x_train=train_x
x_test=test_x

y_train=pd.get_dummies(y_train)

y_test=pd.get_dummies(y_test)
y_test[0:5]

# from sklearn.utils import shuffle
# x_train, y_train=shuffle(x_train,y_train)
# x_test,y_test=shuffle(x_test,y_test)
x_train.shape
x_test.shape

#create the mlp...cnn already trained..
from keras.layers import Dropout
from keras import regularizers
model=Sequential()
model.add(Dense(2000,input_dim=25088,activation='relu',kernel_initializer='uniform'))
model.add(Dropout(0.1))
model.add(Dense(2000,activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(1000,activation='relu'))
model.add(Dropout(0.1))
#,activity_regularizer=regularizers.l1(0.01)
model.add(Dense(500,activation='relu'))
model.add(Dense(500,activation='relu'))
model.add(Dense(output_dim=6,activation='softmax'))


from keras.optimizers import SGD
sgd= SGD(lr=0.001)
model.compile(optimizer=sgd,loss='categorical_crossentropy',metrics=['accuracy'])

#fitting model....
model.summary()
model.save_weights("model_first.h5")

model.fit(x_train,y_train,epochs=10,batch_size=50,validation_data=(x_test,y_test),verbose=True)

# MAKE SOME CHANGES IN HYPER-PARA TO FURTHER INCREASE VALIDATION_ACCURACY
from keras.callbacks import History
hist=History()
model=Sequential()
model.add(Dense(2000,input_dim=25088,activation='relu',kernel_initializer='uniform'))
model.add(Dropout(0.1))
model.add(Dense(2000,activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(1000,activation='relu',activity_regularizer=regularizers.l1(0.00001)))
model.add(Dropout(0.1))
#activity_regularizer=regularizers.l1(0.01)
model.add(Dense(500,activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(500,activation='relu'))
model.add(Dense(output_dim=6,activation='softmax'))


from keras.optimizers import SGD
sgd= SGD(lr=0.0021)
model.compile(optimizer=sgd,loss='categorical_crossentropy',metrics=['accuracy'])
model.summary()

model.fit(x_train,y_train,epochs=21,batch_size=50,validation_data=(x_test,y_test),verbose=True,callbacks=[hist])

#Training is done and training results are...
import matplotlib.pyplot as plt
fig = plt.figure()
im=plt.plot(hist.history['acc'])
plt.title("TRAINING ACCURACY DURING 20 EPOCHS")
fig.savefig('loss_accuracy.png')

fig = plt.figure()
plt.plot(hist.history['val_acc'])
plt.title("VALIDATION ACCURACY DURING 20 EPOCHS")
fig.savefig('validation_accuracy.png')

fig = plt.figure()
plt.plot(hist.history['loss'])
plt.title("TRAINING LOSS VALUES DURING 20 EPOCHS")
fig.savefig('loss_training.png')

#PREDICTION OF VALIDATION DATA..
y_pred=model.predict(x_test)

y_pred[0:5]
#y_test=np.array(y_test)

pred_results= pd.DataFrame(columns=['label'])
y_pred=pd.DataFrame(y_pred)
pred_results=pd.DataFrame()
for i in range(y_pred.shape[0]):
  max_val=max(y_pred.iloc[i])
  for j in range(0,6):
    if(y_pred.iloc[i][j]==max_val):
      if(j==0):
        pred_results = pred_results.append({'label': 'zipper'}, ignore_index=True)
      elif(j==1):
        pred_results = pred_results.append({'label': 'backstrap'}, ignore_index=True)
      elif(j==2):
        pred_results = pred_results.append({'label': 'slip_on'}, ignore_index=True)      
      elif(j==3):
        pred_results = pred_results.append({'label': 'lace_up'}, ignore_index=True)   
      elif(j==4):
        pred_results = pred_results.append({'label': 'buckle'}, ignore_index=True)   
      elif(j==5):
        pred_results = pred_results.append({'label': 'hook&look'}, ignore_index=True)

pred_results['label'].value_counts()

#ACCURACY AND OTHER METRIC SCORES
scores=model.evaluate(x_test,y_test)

print("\n ACCURACY MEAN SCORE: ",scores[1]*100)

#results are pretty decent..

#SAVING MY MODEL....
model_json = model.to_json()
with open("model_final_optimized.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model_final_optimized.h5")
print("Saved model locally")

#USE THIS TO MAKE PREDICTIONS ON ANY CSV
import numpy as np
import pandas as pd
print("\n Enter the CSV file path from current directory, along with extension .csv")
pred_path=input()
testing_data=pd.read_csv(pred_path)
pred_values=prediction(testing_data)

pred_results= pd.DataFrame(columns=['label'])
for i in range(pred_values.shape[0]):
  max_val=max(pred_values.iloc[i])
  for j in range(0,6):
    if(pred_values.iloc[i][j]==max_val):
      if(j==0):
        pred_results = pred_results.append({'label': 'zipper'}, ignore_index=True)
      elif(j==1):
        pred_results = pred_results.append({'label': 'backstrap'}, ignore_index=True)
      elif(j==2):
        pred_results = pred_results.append({'label': 'slip_on'}, ignore_index=True)      
      elif(j==3):
        pred_results = pred_results.append({'label': 'lace_up'}, ignore_index=True)   
      elif(j==4):
        pred_results = pred_results.append({'label': 'buckle'}, ignore_index=True)   
      elif(j==5):
        pred_results = pred_results.append({'label': 'hook&look'}, ignore_index=True)
        
pred_results.to_csv('Predicted_results.csv',index=False)
print("Check your current local directory for the Resultant CSV file")


def prediction(inp):
  test=inp
  test=str(test)
  for i in range(0,test.shape[0]):
    
    ur=list(test.iloc[i])
    ur=ur[1:-1]
    count=0
    for j in ur:
        count+=1
        img_name=j.split("/",6)[-1]+"_"+j.split("/",6)[-2]
        fin="Prediction_images/"+"/image-"+str(count)
        img=urlr.urlretrieve(j,fin)
    
    test_x=[]            
    test_path="Prediction_images"
    for j in range(test.shape[0]):
      ti=image.load_img(test_path+"image-"+str(j)+".jpg",target_size=(224,224))
      ti=image.img_to_array(ti)
      test_x.append(ti)
    
    pred_data=np.array(test_x)
    pred_data=preprocess_input(pred_data)
    
    from keras.applications import VGG16             
    ml= VGG16(weights='imagenet', include_top=False)
           
    pred_data=ml.predict(pred_data)
    pred_data=pred_data.reshape(pred_data.shape[0],pred_data.shape[1]*pred_data.shape[2]*pred_data.shape[3])
    # load json and create model
    json_file = open('model_final_optimized.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model_final_optimized.h5")
    print("Loaded model from disk")
    model=loaded_model
    pred_val=model.predict(pred_data)
    pred_value=pd.DataFrame(pred_val)             
    return pred_value