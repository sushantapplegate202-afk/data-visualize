from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
  word="Guys looks here to work>>"
  workout=["plank","pushup","jogging","jumping"]
  Diet=["dal","nuts","soyabean","protein"]
  track="Gradually your body become sensitives."
  mindset="Do practice daily at a time."
  return render_template("index.html", work=word, workout=workout,Diet=Diet,track=track,mindset=mindset)


@app.route('/simulation')
def simulation_page():
    return render_template('simulation.html') # यह आपकी नई सिमुलेशन फ़ाइल को खोलेगा

@app.route('/tasks')
def tasks_page():
    return render_template('task.html') # यह ऊपर दिए गए गाइड पेज को लोड करेगा

app.run(debug=True)
    

   