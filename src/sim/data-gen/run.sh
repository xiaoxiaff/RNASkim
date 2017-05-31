#!/usr/bin/env bash

Rscript a.R

python3 formatter.py > formatted.fa

cp formatted.fa ../

cp simulated_reads/sample_01* ../

cp simulated_reads/sample_02* ../
