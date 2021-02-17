from flask import Flask

app  =  Flask(__name__)


@app.route('/<string:name>', methods=['GET', 'POST'])
def helloworld(name):
    return 'olá mundo, {}'.format(name)

if __name__  ==  '__main__'  :

    app.run(debug=True)