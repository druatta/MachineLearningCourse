echo -e "Beginning configuration.\n"

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

hash -r
pip install --user --upgrade --force-reinstall pip
pip install wheel --user
pip install --user --ignore-installed pandas
pip install -I --upgrade sympy -t /home/ec2-user/sympy
pip install -user xlrd

cp -R /usr/lib64/python2.7/dist-packages/numpy /home/ec2-user/numpy
cp -R /usr/lib64/python2.7/dist-packages/scipy /home/ec2-user/scipy
cp -R /usr/lib64/python2.7/dist-packages/matplotlib /home/ec2-user/matplotlib

# need the supporting libraries in place on the desintation host
tar -czvf scipy-stack.tgz /home/ec2-user/*

echo -e "\nConfiguration complete."