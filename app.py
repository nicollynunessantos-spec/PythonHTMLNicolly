from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def início():
    nome = "Turma de programação"
    curso = "Python com HTML"

    return render_template(
        'index.html',
        nome = nome,
        curso = curso
    )

    @app.route('/sobre')
    def sobre():
        return"""
        <h1>sobre o Projeto</h1>
        <p>Esse projeto foi criado usando Python e Flask.</p>
        <a href="> Volta para o inicio</a>
        """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)