# gpx2gc

This is a simple program to convert a GPX file generated from the geocaching.com website to a list containing:
- code of geocache
- name of geocache
- link to the listing
- coordinates

## Usage
To run this script you need **python** and the libraries **bs4** and **re**

To convert gpx run this command:

```
python3 gpx2gc.py <name_of_gpx_file>
```
The output will be saved in the file *name_of_gpx_file*_codes.txt