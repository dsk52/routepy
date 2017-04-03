# -*- coding: utf-8 -*-
from flask import Flask, render_template, abort
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


@app.route('/404')
def abort404():
    abort(404)


@app.errorhandler(404)
def error_handler(error):
    '''
    abort(404) したと時にレスポンスをハンドリングするハンドラ
    '''
    msg = 'Error: {code}\n'.format(code=error.code)
    return msg, error.code


if __name__ == '__main__':
    # start web server
    app.run(
        debug=True,
        host='0.0.0.0'
    )
