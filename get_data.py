#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 roshan <roshan@roshan-ThinkPad-T440p>
#
# Distributed under terms of the MIT license.

"""
Continous Machine learning
Data:`DVC` 
"""
import os 
import wget

url='https://md-datasets-cache-zipfiles-prod.s3.eu-west-1.amazonaws.com/yshdbyj6zy-1.zip'
zip_name= "data.zip"
wget.download(url, zip_name)

#Unzip it & Standard the .csv filename

import zipfile
with zipfile.ZipFile(zip_name, "r") as zip_ref:
    zip_ref.filelist[0].filename = 'data_raw.csv'
    zip_ref.extract(zip_ref, filelist[0])

os.remove(zip_name)

