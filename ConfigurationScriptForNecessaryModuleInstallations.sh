#! /usr/bin/env bash

# Install the SciPy stack on Amazon Linux and prepare it for AWS Lambda

sudo yum -y update
sudo yum -y groupinstall "Development Tools"
sudo yum -y install blas --enablerepo=epel
sudo yum -y install lapack --enablerepo=epel
sudo yum -y install atlas-sse3-devel --enablerepo=epel
sudo yum -y install Cython --enablerepo=epel
sudo yum -y install python27
sudo yum -y install python27-numpy.x86_64
sudo yum -y install python27-numpy-f2py.x86_64
sudo yum -y install python27-scipy.x86_64
sudo yum -y install python27-matplotlib.x86_64

cd /home/ec2-user
pip install pandas -t /home/ec2-user/pandas
pip install sympy -t /home/ec2-user/sympy

cp -R /usr/lib64/python2.7/dist-packages/numpy /home/ec2-user/numpy
cp -R /usr/lib64/python2.7/dist-packages/scipy /home/ec2-user/scipy
cp -R /usr/lib64/python2.7/dist-packages/matplotlib /home/ec2-user/matplotlib

# need the supporting libraries in place on the desintation host
tar -czvf scipy-stack.tgz /home/ec2-user/*
# could easily edit to copy to S3 or push to a repo