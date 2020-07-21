from flask import Flask, render_template, url_for, redirect, request, jsonify
from text_summarizer import spacy_summarizer, nltk_summarizer

app = Flask(__name__, template_folder='template')
app.config['SECRET_KEY'] = 'FKDJFKSLERJEWJRKKSDFNKSDJKEORIEWR'

@app.route('/', methods=['GET', 'POST'])
def summarizer():
	if request.method == 'POST':
		raw_text = request.form['raw_text']	
		spacy_summary = spacy_summarizer(raw_text)
		nltk_summary = nltk_summarizer(raw_text)
		return render_template('index.html', spacy_summary=spacy_summary, nltk_summary=nltk_summary, request=1)
	return render_template('index.html', request=0)

if __name__ == '__main__':
	app.run(debug=True)