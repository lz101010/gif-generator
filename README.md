# GIF Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Generate animated GIFs from a series of PNGs. 

## Quick Guide
Install a recent version of [Python](https://www.python.org/downloads/) and [Pillow](https://pypi.org/project/Pillow/):
```shell
$ pip install Pillow
```
Drop the PNG files in `/data` and run 
```sh
$ python generate-gif.py
```
to produce `result.gif`. The PNG files will be appended in alphabetical order for a duration of 100 ms. 


## Configuration
To change the duration, pass an additional argument to the script, e.g.
```sh
$ python generate-gif.py 500
```

To render text over the images, edit `/data/mapping.csv`.
