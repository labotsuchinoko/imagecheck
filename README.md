

## setup ubuntu-14.04 python2.7 64bit 

    $ wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
    $ bash Miniconda2-latest-Linux-x86_64.sh
    #### relogin
    $ sudo apt-get install python-opencv
    $ sudo apt-get update
    $ conda create -n py27-anaconda python=2.7 anaconda
    $ source activate py27-anaconda
    $ pip install -r requirements.txt
    $ cd miniconda2/envs/py27-anaconda/
    $ git clone https://github.com/tushinokooyabun/imagecheck
    $ cd imagecheck
    $ python app.py &


## how to use

    go http://foo.bar.com:3000/
    set a image url.
    and then submit.
