echo "Installing ENS ..."
sudo apt-get install  build-essential python-dev python-numpy python-setuptools python-scipy
pip install -r requirements.txt --no-index --find-links file:///tmp/packages
sudo python setup.py install
