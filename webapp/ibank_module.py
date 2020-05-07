from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def entry_page() -> 'html':
    return render_template('entry.html', the_title="Welcome to Demir/Kicb ibank!")

@app.route("/cancel", methods=["POST"])
def trantransaction() -> 'html':
    title = "Вы успешно отменили транзакцию!!!"
    return render_template('results.html', the_title = title)

if __name__ == '__main__':
    app.run(debug=True)
