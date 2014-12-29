#!/bin/sh
echo ''
python tests.py
echo ''
cd controller/api/tests/
python maps_test.py
echo ''
python wiki_test.py
echo ''
python yelp_test.py 
echo ''
python unicode_test.py