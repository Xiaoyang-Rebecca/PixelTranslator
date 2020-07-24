#!/bin/sh
#SBATCH -N 1	  # nodes requested
#SBATCH -n 20     #number of cores
#SBATCH -p gpu      #node type
#SBATCH -o /uhpc/roysam/xiaoyang/Project_leaf/Codes/pix2pix-tensorflow/outfile  # send stdout to outfile
#SBATCH -e /uhpc/roysam/xiaoyang/Project_leaf/Codes/pix2pix-tensorflow/errfile  # send stderr to errfile
#SBATCH -t 1:00:00  # time requested in hour:minute:second
module add tensorflow/1.2
module add python/3.6.0
cd /uhpc/roysam/xiaoyang/Project_leaf/Codes/pix2pix-tensorflow/
python3.6 main_test_demo.py --phase test_demo --dataset_name=GANinput_vein --epoch=1 --checkpoint_dir='./checkpoint/GANoutput_vein' --sample_dir='./sample/GANoutput_vein' --test_dir='./test/GANoutput_demo'