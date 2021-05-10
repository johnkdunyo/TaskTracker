from flask import Flask, render_template




TaskTracker = Flask(__name__)


@TaskTracker.route('/')
def Home():
    return render_template('home.html')


@TaskTracker.route('/try')
def Try():
    return render_template('try.html')

@TaskTracker.route('/original')
def ori():
    return render_template('try2.html')




if __name__ == '__main__':
    TaskTracker.run(debug=True)