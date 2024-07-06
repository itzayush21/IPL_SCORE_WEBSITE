import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy as np
df = pd.read_csv('df (1).csv')

df = df.dropna(subset=['score'])
x= df.drop(['score'], axis=1)
y= df['score']
x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.20,random_state=0)

model_forest= RandomForestRegressor()
model_forest.fit(x_train,y_train)
y_pred=model_forest.predict(x_test)


def score_predict(batting_team, bowling_team, runs,overs, runs_last_5, wickets_last_5, model=model_forest):
  prediction_array = []
  # Batting Team
  if batting_team == 'Chennai Super Kings' or batting_team == 'CSK' :
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
  elif batting_team == 'Delhi Daredevils' or batting_team == 'DD':
    prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
  elif batting_team == 'Kings XI Punjab' or batting_team == 'KXIP':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
  elif batting_team == 'Kolkata Knight Riders' or batting_team == 'KKR':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
  elif batting_team == 'Mumbai Indians'or batting_team == 'MI':
    prediction_array = prediction_array + [0,0,0,0,1,0,0,0]
  elif batting_team == 'Rajasthan Royals'or batting_team == 'RR':
    prediction_array = prediction_array + [0,0,0,0,0,1,0,0]
  elif batting_team == 'Royal Challengers Bangalore'or batting_team == 'RCB':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0]
  elif batting_team == 'Sunrisers Hyderabad' or batting_team == 'SRH':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,1]
  # Bowling Team
  if bowling_team == 'Chennai Super Kings'or bowling_team == 'CSK':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
  elif bowling_team == 'Delhi Daredevils' or bowling_team == 'DD':
    prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
  elif bowling_team == 'Kings XI Punjab' or bowling_team == 'MI':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
  elif bowling_team == 'Kolkata Knight Riders' or bowling_team == 'KKR':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
  elif bowling_team == 'Mumbai Indians' or bowling_team == 'MI':
    prediction_array = prediction_array + [0,0,0,0,1,0,0,0]
  elif bowling_team == 'Rajasthan Royals'or bowling_team == 'RR':
    prediction_array = prediction_array + [0,0,0,0,0,1,0,0]
  elif bowling_team == 'Royal Challengers Bangalore'or bowling_team == 'RCB':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0]
  elif bowling_team == 'Sunrisers Hyderabad'or bowling_team=='SRH':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,1]
  prediction_array = prediction_array + [runs, overs, runs_last_5, wickets_last_5]
  prediction_array = np.array([prediction_array])
  pred = model.predict(prediction_array)
  return int(pred[0])


score=score_predict(batting_team="RR", bowling_team="RCB", overs=10.2, runs=69,  runs_last_5=38, wickets_last_5=0)
print(score,"||Actual score:164")