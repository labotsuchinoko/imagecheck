

## setup ubuntu-14.04 python2.7 64bit 

    $ wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
    $ bash Miniconda2-latest-Linux-x86_64.sh
    #### relogin
    $ sudo apt-get install python-opencv
    $ sudo apt-get update
    $ conda create -n py27-anaconda python=2.7 anaconda
    $ source activate py27-anaconda
    $ conda install -c https://conda.binstar.org/jjhelmus opencv
    $ cd miniconda2/envs/py27-anaconda/
    $ git clone https://github.com/tushinokooyabun/imagecheck
    $ cd imagecheck
    $ pip install -r requirements.txt
    $ pip install peewee

## how to use cli mode
    $ python listapi.py http://hogehoge.com/images.jpg
    or
    $ python listapi.py list

## how to serve only flask application on 3001

    $ source activate py27-anaconda
    $ python flaskapp.py

    go http://this-host:3001/ using browser.
    set a image url.
    and then submit.

## how to serve flask application gunicorn without nginx on 3001

    $ source activate py27-anaconda
    $ cd ~/miniconda2/envs/py27-anaconda/imagecheck
    $ pip install gunicorn
    $ sudo cp gunicorn-systemd-config/flaskapp.service /etc/systemd/system/
    $ sudo vi /etc/systemd/system/flaskapp
    ExecStart=/home/tsuchinoko/miniconda2/envs/py27-anaconda/bin/gunicorn -w 3 -b 0.0.0.0:3001 wsgi:app
    #ExecStart=/home/tsuchinoko/miniconda2/envs/py27-anaconda/bin/gunicorn -w 3 -b unix:flaskapp.sock wsgi:app    
    $ sudo systemctl start flaskapp
    $ sudo systemctl enable flaskapp 

    go http://this-host:3001/ using browser.
    set a image url.
    and then submit.

## how to serve flask application gunicorn with nginx on 3001

    $ sudo apt-get install nginx
    $ cd ~/miniconda2/envs/py27-anaconda/imagecheck
    $ vi nginx-config/flaskapp
    #ExecStart=/home/tsuchinoko/miniconda2/envs/py27-anaconda/bin/gunicorn -w 3 -b 0.0.0.0:3001 wsgi:app
    ExecStart=/home/tsuchinoko/miniconda2/envs/py27-anaconda/bin/gunicorn -w 3 -b unix:flaskapp.sock wsgi:app
    $ sudo cp nginx-config/flaskapp /etc/nginx/sites-available/
    $ sudo ln -s /etc/nginx/sites-available/flaskapp /etc/nginx/sites-enabled
    $ sudo nginx -t
    $ sudo systemctl restart nginx

    go http://this-host:3001/ using browser.
    set a image url.
    and then submit.
