#!/bin/bash

[[ -e sqlite.db ]] || ./server.py create_db
./server.py

