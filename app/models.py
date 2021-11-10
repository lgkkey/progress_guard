#!/usr/bin/python3
#_*_ coding:utf-8 _*_

import os
import signal

def get_process(cmd):
    return os.popen(cmd).read().split('\n')

def ones(datas):
    cc=[]
    for d in datas:
        if len(d)<1:
            continue
        temp=[c for c in d.split(' ') if c]
        cc.append(temp)
    return cc

def doit(cmd):
    return ones(get_process(cmd))
    
    
def kill_pro(pid):
    message="success"
    try:
        pgid=os.getpgid(pid)
        os.killpg(pgid,signal.SIGTERM)
    except ProcessLookupError as err:
        message="不存在该进程"
    except PermissionError as err:
        message="无操作权限"
    return message
def restart_pro(pid,cmd):
    message="success"
    try:
        if len(cmd) >1 :
            re=doit("ps -ef |grep '" +cmd+"' |grep -v grep ")
        else:
            return "命令错误"
        if (len(re)>0):
            message=kill_pro(pid)
            if (message!="success"):
                return message
        cmd_re=os.system("nohup "+cmd+ " >/dev/null 2>&1 &")

    except PermissionError as err:
        pass
    return message

def get_top():
    sysinfo ={}
    top=os.popen("top -bi -n 1").read().split('\n\n')[0].split('\n')
    top1=[d for d in top[0].replace(',',' ').split(' ') if d]
    sysinfo['time']=top1[2]
    sysinfo['uptime']='-'.join(top1[4:7])
    sysinfo['users']=top1[7]
    sysinfo['loadavg']=top1[11:14]
    top2=[d for d in top[1].replace(',',' ').split(' ') if d]
    sysinfo['proc_num']=top2[1]
    sysinfo['running']=top2[3]
    sysinfo['sleeping']=top2[5]
    sysinfo['stopped']=top2[7]
    sysinfo['zombie']=top2[9]
    topcpus=[d for d in top[2].replace(',',' ').split(' ') if d]
    sysinfo['us']=topcpus[1]
    sysinfo['sy']=topcpus[3]
    sysinfo['ni']=topcpus[5]
    sysinfo['id']=topcpus[7]
    sysinfo['wa']=topcpus[9]
    sysinfo['hi']=topcpus[11]
    sysinfo['si']=topcpus[13]
    sysinfo['st']=topcpus[15]
    topmem=[d for d in top[-2].replace(',',' ').split(' ') if d]
    sysinfo['memtotal']=topmem[3]
    sysinfo['memfree']=topmem[5]
    sysinfo['memused']=topmem[7]
    sysinfo['membuff']=topmem[9]
    topswap=[d for d in top[-1].replace(',',' ').split(' ') if d]
    sysinfo["swaptotal"]=topswap[2]
    sysinfo["swapfree"]=topswap[4]
    sysinfo["swapused"]=topswap[6]
    sysinfo["swapcache"]=topswap[8]
    return sysinfo



