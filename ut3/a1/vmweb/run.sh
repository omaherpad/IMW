#!/bin/bash

source /home/alu5627/.virtualenvs/vmweb/bin/activate
uwsgi --ini /home/alu5627/vmweb2/uwsgi.ini
