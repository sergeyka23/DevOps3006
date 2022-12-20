from flask import Flask, request

error = ""

try:
    my_file = open("scores_file.txt", 'r')
    score = my_file.readline()
    my_file.close()

except OSError:
    error = "Error to read score"

my_file.close()

app = Flask("Scores")


@app.route('/')
def my_func():
    if error == "":
        return '<html><head><title>Scores Game</title></head><body><h1>The score is <div id="score">' + score + '</div></h1></body></html>'
    else:
        return '<html><head><title>Scores Game</title></head><body><body><h1><div id="score" style="color:red">' + error + '</div></h1></body></html>'


app.run(host="0.0.0.0", port=5001, debug=False)
