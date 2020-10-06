#!/usr/bin/env python
# coding: utf-8

# In[41]:
import os
cmd = os.system

class File(object):
  files = []

  def __init__(self,name):
    self.name = name
    File.files.append(self)
  
  def remove_spaces(self):
    with open(self.name, 'r') as f:
      lines = f.readlines()
      f.close()
    lines = [line.strip() for line in lines]
    lines = [line + '\n' for line in lines]
    with open(self.name, 'w') as f:
      f.writelines(lines)
      f.close()

def main():
  g = True
  k = True
  while g:
    kind = input("For master enter 'M', for slave enter 'S' and for client enter 'C': ")
    if kind.lower() == 'm':
      name = 'name'
      cmd('mkdir /nn')
      directory = '/nn'
      g = False
    elif kind.lower() == 's':
      name = 'data'
      cmd('mkdir /dn')
      directory = '/dn'
      g = False
    elif kind.lower() == 'c':
      g = False
    else:
      print('Invalid input')

  while k:
    IP = (input('Enter the IP address: '))
    ip = IP.split('.')
    for bit in ip:
      try:
        int(bit)
        k = False
      except ValueError:
        print('Enter integer')

  core = File('core-site.xml')
  f1 = open(core.name,'w')
  f1.write('''<?xml version="1.0"?>
  <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

  <!-- Put site-specific property overrides in this file. -->

  <configuration>

  <property>
  <name>fs.default.name</name>
  <value>hdfs://{}:9001</value>
  </property>

  </configuration>'''.format(IP))
  f1.close()

  if (kind.lower() == 'm') or (kind.lower() == 's'):
    hdfs = File('hdfs-site.xml')
    f2 = open(hdfs.name,'w')
    f2.write('''<?xml version="1.0"?>
    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

    <!-- Put site-specific property overrides in this file. -->

    <configuration>
                
    <property>
    <name>dfs.{}.dir</name>
    <value>{}</value>
    </property>

    </configuration>'''.format(name,directory))
    f2.close()
            
  for file in File.files:
    file.remove_spaces()
      
  cmd('cp core-site.xml /etc/hadoop')
  if (kind.lower() == 'm') or (kind.lower() == 's'):
    cmd('cp hdfs-site.xml /etc/hadoop')

  if kind.lower() == 'm':
    cmd('hadoop namenode -format')
    cmd('hadoop-daemon.sh start namenode')
  elif kind.lower() == 's':
    cmd('hadoop-daemon.sh start datanode')
if __name__ == '__main__':
  main()