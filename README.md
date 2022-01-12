# VRDL HW4 - Image super resolution
###### tags: `基於深度學習之視覺辨識專論`
## Introduction

In this assignment, we are given we are given 291 high-resolution training images and 14 low-resolution testing images. Our goal is to train a model to reconstruct a x3 high-resolution image from a low-resolution image. In this assignment, I use my EDSR as my approach to do image super resolution task. This project is modified from [Saafke/EDSR_Tensorflow](https://github.com/Saafke/EDSR_Tensorflow).

![](https://i.imgur.com/begkDI0.png)


## Environment
### Hardware
* CPU: Intel i5-7500 CPU
* GPU: NVIDIA GeForce GTX 1060 6GB

## Conda environment
The used packages are listed in: [requirement.txt](https://drive.google.com/file/d/1BcI58RvXzoNWdxwM2JTQGtCH2xiO2OzQ/view?usp=sharing)

Then, you can create a conda environment named `EDSR(py3.6)` by the command:
```
conda create --name EDSR(py3.6) --file requirements.txt
```

## Installation
Clone or download this project.

Or install the original project: [Saafke/EDSR_Tensorflow](https://github.com/Saafke/EDSR_Tensorflow), then copy and paste my `main.py` into it.

## Prepare dataset
1. Create a folder named `dataset` under the project directory.
2. Put the given dataset: `training_hr_images` and `testing_lr_images`, under `dataset` folder.
3. (Optional) Use `aug.py` to augment `training_hr_images` in order to generate more training data.

## Train & Test
Make sure you activate the conda environment first. Here are some example commands I've used.

### Train
Run this command to train from scratch:
```
python main.py --train --fromscratch --scale 3 --traindir dataset/training_hr_images --validdir dataset/testing_lr_images --epochs 30 --F 320
```
Continue training from previous checkpoint:
```
python main.py --train --scale 3 --traindir dataset/training_hr_images --validdir dataset/testing_lr_images --epochs 10 --F 320
```

### Test (Inference)
To test the model and generate pred images:
* Create two folders named `CKPT_dir` and `images` under the project directory.
* Create a folder name `x3`. Put these [model checkpoint files](https://drive.google.com/drive/folders/1s5_qiJfcxCVBtyB1M8CHkgVTPopQcNTY?usp=sharing) under `CKPT_dir/x3`. 
* Then, run this command:
```
python main.py --upscale --scale 3
```
After execution, the result images will be in `images` folder.



## Results
| Low-resolution testing image | Bicubic x3 | EDSR x3 |
| :-: | :-: | :-: |
| ![](https://i.imgur.com/GQEwzAY.png) | ![](https://i.imgur.com/KRhfneK.png) | ![](https://i.imgur.com/yjbti6X.png) | 
| ![](https://i.imgur.com/09RUAHQ.png)| ![](https://i.imgur.com/GrjIAU4.png) | ![](https://i.imgur.com/LDarg4v.png) |
| ![](https://i.imgur.com/uVsC4Yn.png) | ![](https://i.imgur.com/aQ7w5Ma.png) | ![](https://i.imgur.com/eAoxM65.png) |


| Model Name  | PSNR on CodaLab |
| :-: | :-: |
| [Best](https://drive.google.com/drive/folders/1s5_qiJfcxCVBtyB1M8CHkgVTPopQcNTY?usp=sharing)  | 27.2928 |
