#!/usr/bin/python3
#_*_ coding:utf-8 _*_
from app import app
from flask import request,make_response,url_for,redirect,render_template
from app.models import doit,print_proc,kill_pro,restart_pro,get_top


@app.route('/')
def index():
    return '<h1>hello world </h1><br><h3><a href="/control">点击跳转</a>到管理界面</h3>'
	
@app.route('/get')
def get_proc():
    resp={'body':""}
    resp['body']=doit("ps  -ef")[1:]
    return resp

@app.route('/search')
def search():
    args=request.args.get('key') or ''
    resp={'body':""}
    resp['body']=doit("ps -ef|grep '"+args+"'|grep -v grep")
    return resp

@app.route('/control')
def test():
    return render_template("display.html")
@app.route("/kill")
def kill_p():
    args=int(request.args.get('pid') or -1)
    if args<0:
        pass
    else:
        mes= kill_pro(args)

    return mes
@app.route("/restart")
def restart_p():
    pid=int(request.args.get('pid') or '-1')
    cmd=request.args.get('cmd') or ' '
    mesg=restart_pro(pid,cmd);
    return mesg
@app.route('/top')
def gettop():
    return get_top()


