"""
This routine mimics a subset of fucntionalities of linux's OD command in windows.
Author: Sukhbinder Singh
Date: 10 Oct 2016
"""

from struct import unpack
import argparse
import sys

# Helper functions
def ReadDbl(data):
    return unpack('@d',data)[0]
def ReadLng(data):
    return unpack('@q',data)[0]

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Mimic OD (Octal Dump) functionality with python ")
    parser.add_argument("-j","--skip-bytes",help="skip BYTES input bytes first",type=int)
    parser.add_argument("-N","--read-bytes",help="limit dump to BYTES input bytes",type=int)
    parser.add_argument("-t","--format",help="select output format or formats: d8 for int (default), f8 for float",default='d8',choices=['d8','f8'])
    parser.add_argument("filename",help="filename")
    args = parser.parse_args()
# Verifying filename
    try:
        fd=open(args.filename,'rb')
    except:
        print " \n\n Error opening file: " + args.filename +" \n\n "
        sys.exit(1)
# If skipbytes skip bytes
    if args.skip_bytes:
        fd.seek(args.skip_bytes)
#
# Read and display results
    i=0
    while (True):
        try:
            data=fd.read(8)
            if args.format =='f8':
                print ReadDbl(data) 
            else:
                print ReadLng(data)
            i+=8
            if args.read_bytes:
                if i+8 > args.read_bytes:
                    break
        except:
            break
# Close file after read
    fd.close()

