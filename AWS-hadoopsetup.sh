yum -y install python3
pip3 install gdown 
cd /root
gdown --id 1541gbFeGZZJ5k9Qx65D04lpeNBw87rM5
gdown --id 17UWQNVdBdGlyualwWX4Cc96KyZhD-lxz
rpm -ivh jdk-8u171-linux-x64.rpm
rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force
python3 AWSHadoopSetup-CLI_Tool/AWS-hadoop.py