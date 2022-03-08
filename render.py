from flask import Flask, render_template

import data_

app = Flask(__name__)

@app.route('/search')
def search():
    videos = data_.get_results_from_keyword(keyword = 'dude perfect')
    return render_template('search.html', videos = videos)

if __name__ == '__main__':
    app.run()

