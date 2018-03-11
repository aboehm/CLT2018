from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    my_list = ["Item 1", "Item 2", "Item 3"]
    # Template unter 'templates/index.html' rendern
    # 'my_list' wird als Variable bekannt gemacht
    return render_template('index.html', my_list=my_list)


if __name__ == '__main__':
    app.run()
