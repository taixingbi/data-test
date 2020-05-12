#!/bin/bash
# -------------------------
# example on how to launch the wer calculation script from a bash command line
python3 ./code/werlev.py ./sample_input_files/TEST1_REFERENCE_norm_manually_checked.txt ./sample_input_files/TEST1_TLGeneral_output_norm.txt ./sample_output_files/TEST1_TLGeneral_WER.txt 1
python3 ./code/werlev.py ./sample_input_files/TEST1_REFERENCE_norm_manually_checked.txt ./sample_input_files/TEST1_TLSpecific_output_norm.txt ./sample_output_files/TEST1_TLSpecific_WER.txt 1
python3 ./code/werlev.py ./sample_input_files/TEST1_REFERENCE_norm_manually_checked.txt ./sample_input_files/TEST1_Google_output_norm.txt ./sample_output_files/TEST1_Google_WER.txt 1
python3 ./code/werlev.py ./sample_input_files/TEST1_REFERENCE_norm_manually_checked.txt ./sample_input_files/TEST1_AWS_output_norm.txt ./sample_output_files/TEST1_AWS_WER.txt 1
