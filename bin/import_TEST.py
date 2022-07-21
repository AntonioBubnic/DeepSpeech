#!/usr/bin/env python
import os
import pandas
import sys

df = pandas.DataFrame(
    data=[(os.path.abspath("data/test/4ab96362a9e1e514860c8b19787051a8.wav"), os.path.getsize("data/test/test1_tekst.txt"), transcript)],
    columns=["wav_filename", "wav_filesize", "transcript"],
)
df.to_csv(os.path.join("data/test", "test_excel1.csv"), index=False)

#df = pandas.DataFrame(
#data=[(os.path.abspath(local_file), os.path.getsize(local_file), transcript)],
#columns=["wav_filename", "wav_filesize", "transcript"],
#)
#df.to_csv(os.path.join(data_dir, "ldc93s1.csv"), index=False)#