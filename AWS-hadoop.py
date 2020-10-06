#!/usr/bin/env python
# coding: utf-8

# In[41]:
import os
cmd = os.system

def remove_spaces(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        f.close()
    lines = [line.strip() for line in lines]
    lines = [line + '\n' for line in lines]
    with open(file, 'w') as f:
        f.writelines(lines)
        f.close()

def main():
    core = 'core-site.xml'
    hdfs = 'hdfs-site.xml'
    g = True
    while g:
        kind = input("For master enter 'M' & for slave enter 'S': ")
        while k:
            IP = (input('Enter the IP address: '))
            ip = IP.split('.')
            for bit in ip:
                try:
                    int(bit)
                    k = False
                except:
                    print('Enter integer')
        if kind.lower() == 'm':
            name = 'name'
            cmd('mkdir /nn')
            directory = '/nn'
            g = False
        elif kind.lower() == 's':
            k = True
            name = 'data'
            cmd('mkdir /dn')
            directory = '/dn'
            g = False
        else:
            print('Invalid input')

    f1 = open(core,'w')
    f1.write('''<?xml version="1.0"?>
    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

    <!-- Put site-specific property overrides in this file. -->

    <configuration>

    <property>
    <name>fs.default.name</name>
    <value>hdfs://{}:9001</value>
    </property>

    </configuration>'''.format(IP))

    f2 = open(hdfs,'w')
    f2.write('''<?xml version="1.0"?>
    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

    <!-- Put site-specific property overrides in this file. -->

    <configuration>
            
    <property>
    <name>dfs.{}.dir</name>
    <value>{}</value>
    </property>

    </configuration>'''.format(name,directory))
            
    f1.close()
    f2.close()
    for file in (core,hdfs):
        remove_spaces(file)
    cmd('cp core-site.xml /etc/hadoop')
    cmd('cp hdfs-site.xml /etc/hadoop')

    if kind.lower() == 'm':
        cmd('hadoop namenode -format')
        cmd('hadoop-daemon.sh start namenode')
    elif kind.lower() == 's':
        cmd('hadoop-daemon.sh start datanode')
if __name__ == '__main__':
    main()

