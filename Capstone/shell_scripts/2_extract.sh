#!/bin/bash

'''
Extract needed website urls according to line number.
Modify following parameters.
'''

start=1
end=10

cat 1_SplitUrls.txt | tail -n +$(($start+1)) | head -n +$(($end-$start+1)) > 2_ExtractUrls.txt
