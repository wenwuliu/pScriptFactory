#!/bin/zsh
# author:liuwenwu
# desc:
# create date:2022-02-08 22:29:34

dir=`pwd`
home=`echo ~`
fullDir=$dir/script/$1/
file=$fullDir/$1.py
if [ -d $fullDir ];then
    echo "building ..."
    cd $fullDir
    sudo pyinstaller --log-level=ERROR --clean -y $file
    sudo mv dist/$1/$1 dist/$1/$1.pybn
    sudo cp -R -f dist/$1 $home/.self-built-command/common/$1
    sudo rm -rf dist
    sudo rm -rf build
    sudo rm $1.spec
    echo "build success!"
else
    echo "file or directory not exist"
fi
