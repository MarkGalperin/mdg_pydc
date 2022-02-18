# mdg_pydc
A package for controlling the FLIR Flea3 camera with simple, terse commands. 

## Prerequisites
- clone this repository
```sh
git clone https://github.com/MarkGalperin/mdg_pydc
```
- install `pydc1394` and the python image library
```sh
pip install pydc1394
pip install PIL
```

## Usage
See `camera_capture.py` for an example of single-shot usage

Initialize the camera with `init_camera()`

```python
cam0 = init_camera()
```

Then command the camera to take an image with `caputure_one`

```python
capture_one(cam0,path)
```
