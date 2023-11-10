from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'job': 'job1',
    'description': 'check your house'
  },
  {
    'id':2,
    'job': 'job2',
    'description': 'visit your house'
  },
  {
    'id':3,
    'job': 'job3',
    'description': 'send your report'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)
  
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=4000, debug=True)