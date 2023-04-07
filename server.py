from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html', times=3, color='aqua')

@app.route('/play/<int:times>')
def play_times(times):
    return render_template('index.html', times=times, color='aqua')

@app.route('/play/<int:times>/<string:color>')
def play_color(times, color):
    return render_template('index.html', times=times, color=color)

if __name__ == '__main__':
    app.run(debug=True)
