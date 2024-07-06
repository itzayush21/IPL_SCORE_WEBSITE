from flask import Flask, render_template, request,session
from algo import score_predict

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
  if request.method=="POST":
    team_1 = request.form.get('team1Hidden')
    team_2 = request.form.get('team2Hidden')
    overs = request.form.get('overs')
    runs = request.form.get('runs')
    run_last_5 = request.form.get('run_last_5')
    wicket_last_5 = request.form.get('wicket_last_5')
  
    
    s = score_predict(team_1, team_2, overs, runs, run_last_5, wicket_last_5)
    return render_template('index.html', s=s)

  return render_template('index.html')



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
