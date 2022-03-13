# Low Precision Yolo

This repo contains code for training Yolo(v1, v3, v5) architectures using different quantization. It utilizes [Brevitas](https://github.com/Xilinx/brevitas) which is a Pytorch research library for quantization-aware training (QAT) from Xilinx. The code is developed on top of [YOLOV5](https://github.com/ultralytics/yolov5).


## Installation

```bash
$ git clone https://github.com/sefaburakokcu/quantized-yolov5
$ cd yolov5
$ pip install -r requirements.txt
```


## Inference

`detect.py` runs inference on a variety of sources and saving results to `runs/detect`.

```bash
$ python detect.py --weights /path-to-weights-folder
		    --source 0  # webcam
		            file.jpg  # image 
		            file.mp4  # video
		            path/  # directory
		            path/*.jpg  # glob
		            'https://youtu.be/NUsoVlDFqZg'  # YouTube
		            'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```

## Training

Run commands below to reproduce results
on [Widerface](http://shuoyang1213.me/WIDERFACE/) dataset (dataset auto-downloads on
first use).

```bash
$ python train.py --data widerface.yaml --cfg models/hub/yolov1-tiny-quant.yaml --weights '' --batch-size 128
```

## References

* [YOLOV5](https://github.com/ultralytics/yolov5)
* [BREVITAS](https://github.com/Xilinx/brevitas)

## Authors

- [Sefa Burak OKCU](sefaburak.okcu@gmail.com)
- [Bestami GÜNAY](bestamigunay1@gmail.com)


