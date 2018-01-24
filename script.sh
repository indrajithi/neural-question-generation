#!/bin/bash  
cd sentence
th translate.lua -model new_840B.300d.600rnn_epoch15_25.85.t7 -config newcfg -output ../gendata/quest.txt