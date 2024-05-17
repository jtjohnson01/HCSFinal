from flask import Flask, render_template, request
from services import translate, search, graph


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    searchword = request.form['searchword']

    translatedsearchword = translate.english_to_chinese(searchword)

    counts = search.count_character(translatedsearchword)

    fig1 = graph.make_graph(counts)
    fig2 = graph.make_unique_graph(counts)
    fig3 = graph.make_total_graph(counts)

    fig4 = graph.get_total_characters_graph()
    fig5 = graph.get_unique_characters_graph()

    return render_template('results.html', translation = f'{searchword} &#8594; {translatedsearchword}', graphJSON1=fig1.to_json(), graphJSON2=fig2.to_json(), graphJSON3=fig3.to_json(), graphJSON4=fig4.to_json(), graphJSON5=fig5.to_json())

if __name__ == '__main__':
    app.run()