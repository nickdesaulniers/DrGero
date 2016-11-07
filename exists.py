#!/usr/bin/env python

import os
import sys

def comments(item):
    return not item.startswith('#')

def clean(item):
    return comments(item) and item != '\n'

def check_blobs(blob_path, dev_dir):
    blobs = map(str.rstrip, filter(clean, list(open(blob_path))))
    for blob in blobs:
        check_blob(blob, dev_dir)

def check_blob(blob, dev_dir):
    path = os.path.join(dev_dir, blob[1:])
    exists = os.path.exists(path)
    if exists:
        print 'Exists %s' % path
    else:
        print 'Missing %s' % path
    #print path

if len(sys.argv) > 2:
    check_blobs(sys.argv[1], sys.argv[2])
else:
    print 'usage: ./exists.py path/to/proprietary-blobs.txt path/to/out/target/product/<device>'
