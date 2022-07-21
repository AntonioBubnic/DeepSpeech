#!/usr/bin/env python
import os
import sys
import pandas

from deepspeech_training.util.downloader import maybe_download

df = pandas.DataFrame(
    data=[(os.path.abspath('data/test'), os.path.getsize('data/test'), transcript)],
    columns=["wav_filename", "wav_filesize", "transcript"],
)
df.to_csv(os.path.join('data/test', "test_excel1.csv"), index=False)