import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

data = pd.read_csv("BankNote_Authentication.csv",sep=",")

data = data[['variance', 'skewness', 'curtosis', 'entropy', 'class']]
z= "class"

x=np.array(data.drop([z],1))
y=np.array(data[z])

model = LogisticRegression()
model.fit(x,y)

predictions = model.predict(x)

pickle.dump(model,open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
