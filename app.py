# -*- coding: utf-8 -*-
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index(title='hello, world'):
    return render_template('index.html', title=title)


@app.route('/about')
def about(title='About'):
    '''
    Description:
      - 固定ページ用のテンプレートを使う処理
    '''
    return render_template('page.html', title=title)


@app.route('/archive/<cat>')
def archive(cat):
    '''
    Description:
      - 一覧ページ用のテンプレートを使う処理
    '''
    data = ['hoge', 'fuga', 'boo']
    return render_template('archive.html', title=cat, data=data)


if __name__ == '__main__':
    # start web server
    app.run(
        debug=True,
        host='0.0.0.0'
    )
