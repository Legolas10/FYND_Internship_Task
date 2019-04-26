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
  
  
