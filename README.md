## AWSHadoopSetup-CLI_Tool :raised_hands:

### No muss, no fuss method to setup Hadoop Cluster on AWS Cloud:blush:

#### 1. Go to root directory
```bash
cd /root
```
#### 2. Install git:
```bash 
yum install git
```
#### 3. Clone this repository using the CLI into the root directory
```bash
git clone https://github.com/sukesh2000/AWSHadoopSetup-CLI_Tool.git
```
#### 4. Go inside AWSHadoopSetup-CLI_Tool directory
```bash
cd AWSHadoopSetup-CLI_Tool
```

#### 5. Source the bash file
```bash
source AWS-hadoopsetup.sh
```
#### After this the program will ask you to enter the IP address for core-site.xml file & the type of Hadoop setup you would like to have, enter master, slave or client as required! 
### Wait for the magic to happen :tophat::crystal_ball:

Once the setup is complete, run ```jps``` command to check whether the required Hadoop setup is complete.

Feel free to open an issue if you encounter a bug & PRs for optimizations are most welcome :smile:

![](https://visitor-badge.glitch.me/badge?page_id=sukesh2000.AWSHadoopSetup-CLI_Tool)