#!/bin/bash


echo '欢迎使用'

args=$1
expr $args + 1 >/dev/null 2>&1
if [ $? -ne 0  ]
then
	echo "启动参数错误->退出"
	exit -1
elif [ -z $args ] 
then
	echo "前台启动"
	python3  $PWD/run.py 
else 
	echo "后台延时:$args秒启动"
	sleep $args
	nohup python3  $PWD/run.py >/dev/null 2>err.log &
	echo "正在启动中"
fi


echo "本脚本结束"
