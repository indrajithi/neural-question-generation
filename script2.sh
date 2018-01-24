#!/bin/bash  
cd paragraph
th translate.lua -model 840B.300d.rnn.para_epoch15_28.71.t7 -config newcfg -output ../gendata/quest.txt
