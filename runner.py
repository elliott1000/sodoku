from flask import Flask, render_template, request, redirect, url_for
from websolve import websolve
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
  if request.method == 'POST':
    data = str(request.data)[2:-1]
    global solveds
    global solved
    solved = websolve(data)
    solveds = ''
    for i in solved:
      for r in i:
        solveds += r
    
    
  

  return render_template('indext.html')


@app.route('/answer', methods=['GET', 'POST'])
def answer():
  return render_template('indext.html', solved='"' + str(solveds) + '"')


if __name__ == '__main__':
  app.run(debug=True)