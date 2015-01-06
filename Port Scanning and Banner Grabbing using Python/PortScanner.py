#!/usr/bin/env python

'''
A simple port scanning tool.
If it is able to establish a socket connection with the host:port, the port is open. Else, it is not.

Reference: "Violent Python" by T.J. O'Connor, Syngress 1st edition, November 2008
'''
__author__ = "Emil Tan"

import optparse
from socket import *

def conn(targetHost, targetPort):
    try:
        conn = socket(AF_INET, SOCK_STREAM)
        conn.connect((targetHost, targetPort))
        print '[+] Connection to ' + targetHost + ' port ' + str(targetPort) + ' succeeded!'
    except Exception, e:
        print '[-] Connection to ' + targetHost + ' port ' + str(targetPort) + ' failed: ' + str(e)
    finally:
        conn.close()

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
