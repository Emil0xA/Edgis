#!/usr/bin/env python

'''
A simple port scanning / banner grabbing tool.
If it is able to establish a socket connection with the host:port, the port is open. Else, it is not.
If it is able to establish a socket connection, it will then proceed on to grab the service banner. 

References:
"Violent Python" by T.J. O'Connor, Syngress 1st edition, November 2008
"Banner Grabbing HTTP" Stack Overflow, Question 22746480 (http://stackoverflow.com/questions/22746480/banner-grabbing-http)
'''
__author__ = "Emil Tan"

import optparse
from socket import *

def conn(targetHost, targetPort):
    try:
        conn = socket(AF_INET, SOCK_STREAM)
        conn.connect((targetHost, targetPort))
        print '[+] Connection to ' + targetHost + ' port ' + str(targetPort) + ' succeeded!'
        if targetPort == 80:
            grabHTTP(conn)
        else:
            grab(conn)
    except Exception, e:
        print '[-] Connection to ' + targetHost + ' port ' + str(targetPort) + ' failed: ' + str(e)
    finally:
        conn.close()

def grab(conn):
    try:
        conn.send('Hello, is it me you\'re looking for? \r\n')
        ret = conn.recv(1024)
        print '[+]' + str(ret)
    except Exception, e:
        print '[-] Unable to grab any information: ' + str(e)
        return

def grabHTTP(conn):
    try:
        conn.send('GET  HTTP/1.1 \r\n')
        ret = conn.recv(1024)
        print '[+]' + str(ret)
    except Exception, e:
        print '[-] Unable to grab any information: ' + str(e)
        return

def main():
    parser = optparse.OptionParser("%prog -t <target host(s)> -p <target port(s)>")
    parser.add_option('-t', dest='targetHosts', type='string', help='Specify the target host(s); Separate them by commas')
    parser.add_option('-p', dest='targetPorts', type='string', help='Specify the target port(s); Separate them by commas')

    (options, args) = parser.parse_args()

    if (options.targetHosts == None) | (options.targetPorts == None):
        print parser.usage
        exit(0)

    targetHosts = str(options.targetHosts).split(',')
    targetPorts = str(options.targetPorts).split(',')

    setdefaulttimeout(5)

    for targetHost in targetHosts:
        for targetPort in targetPorts:
            conn(targetHost, int(targetPort))
        print ''

if __name__ == '__main__':
    main()
