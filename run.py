#!usr/bin/python3
#_*_ coding:utf-8 _*_

from app import app
import config

if __name__ == '__main__':
#    app.debug =True
    app.run(host=config.conf["host"],port=config.conf["port"])
