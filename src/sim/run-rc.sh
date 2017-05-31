#!/usr/bin/env bash

GLOG_logtostderr=1 ../rs_cluster  -gene_fasta=formatted.fa -num_threads=4 -output=clustered.fa -rs_length=60

GLOG_logtostderr=1  ../rs_index -transcript_fasta=clustered.fa -index_file=clustered_gene.fa.pb -rs_length=60 -num_threads 4

GLOG_logtostderr=1  ../rs_select -index_file=clustered_gene.fa.pb -selected_keys_file=clustered_gene.fa.sk  -rs_length=60

GLOG_logtostderr=1  ../rs_count  -selected_keys_file=clustered_gene.fa.sk -count_file=clustered_gene.fa.cf -read_files1=sample_01_1.fasta -read_files2=sample_01_2.fasta -num_threads=1

GLOG_logtostderr=1  ../rs_estimate -count_file=clustered_gene.fa.cf > estimation

cat estimation