# Low Precision Yolo

This repo contains code for training Yolo(v1, v3, v5) architectures using different quantization. It utilizes [Brevitas](https://github.com/Xilinx/brevitas) which is a Pytorch research library for quantization-aware training (QAT) from Xilinx. The code is developed on top of [YOLOV5](https://github.com/ultralytics/yolov5).


## Installation

```bash
$ git clone git@github.com:sefaburakokcu/quantized-yolov5.git
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
on [Widerface](http://shuoyang1213.me/WIDERFACE/) dataset.

```bash
$ python train.py --data widerface.yaml --cfg models/hub/yolov1-tiny-quant.yaml --weights '' --batch-size 128
```

## Export

Sigmoid activation is used in detect layer when training whereas HardTanh is used when exporting the model for FINN.

```bash
$ python export.py --data widerface.yaml --weights runs/train/exp1/weights/best.pt --nodetect
```

## Citation

If you utilize this repo in your research, please cite it as:

```
@inproceedings{Gunay_2022, series={EECSS’22},
   title={LPYOLO: Low Precision YOLO for Face Detection on FPGA},
   ISSN={2369-811X},
   url={http://dx.doi.org/10.11159/mvml22.108},
   DOI={10.11159/mvml22.108},
   booktitle={Proceedings of the 8th World Congress on Electrical Engineering and Computer Systems and Science},
   publisher={Avestia Publishing},
   author={Gunay, Bestami and Okcu, Sefa Burak and Bilge, Hasan Sakir},
   year={2022},
   month=jul, collection={EECSS’22} }
```
   
## References

* [YOLOV5](https://github.com/ultralytics/yolov5)
* [BREVITAS](https://github.com/Xilinx/brevitas)

## Authors

- [Sefa Burak OKCU](https://www.linkedin.com/in/sefaburakokcu/)
- [Bestami GÜNAY](https://www.linkedin.com/in/bestamigunay/)


