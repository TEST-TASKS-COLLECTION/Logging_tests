#!/bin/bash

for package in $(pip freeze)
do
pip uninstall $package -y
done