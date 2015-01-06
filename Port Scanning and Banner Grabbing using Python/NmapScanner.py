#!/usr/bin/env python

'''
A simple port scanning tool that utilises the nmap library

Reference: "Violent Python" by T.J. O'Connor, Syngress 1st edition, November 2008
'''
__author__ = "Emil Tan"

import optparse
import nmap

def nmapScan(targetHosts, targetPorts):
    try:
        scanner = nmap.PortScanner()
        scanner.scan(targetHosts, targetPorts)

        for targetHost in scanner.all_hosts():
            if scanner[targetHost].state() == 'up':
                print targetHost + ' is up'
            for targetPort in scanner[targetHost]['tcp']:
                print 'Port ' + str(targetPort) + '/tcp ' + scanner[targetHost]['tcp'][int(targetPort)]['name'] + ' is ' + scanner[targetHost]['tcp'][int(targetPort)]['state']
            print ''
    except Exception, e:
        print '[-] Something bad happened during the scan: ' + str(e)

def main():
    parser = optparse.OptionParser("%prog -t <target host(s)> -p <target port(s)>")
    parser.add_option('-t', dest='targetHosts', type='string', help='Specify the target host(s)')
    parser.add_option('-p', dest='targetPorts', type='string', help='Specify the target port(s)')

    (options, args) = parser.parse_args()

    if (options.targetHosts == None) | (options.targetPorts == None):
        print parser.usage
        exit(0)

    targetHosts = str(options.targetHosts)
    targetPorts = str(options.targetPorts)

    nmapScan(targetHosts, targetPorts)

    '''
    for targetHost in targetHosts:
        for targetPort in targetPorts:
            conn(targetHost, int(targetPort))
        print ''
    '''
if __name__ == '__main__':
    main()