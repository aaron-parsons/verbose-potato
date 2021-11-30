import pandas as pd
import numpy as np

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--size', type=int, dest='size', default=512)
parser.add_argument('--output-dir', type=str, dest='output_dir', default='saved_models_aaron')
parser.add_argument('--output-fname', type=str, dest='output_fname', default='data.parquet.gzip')
args = parser.parse_args()

# make a dataframe
df = pd.DataFrame(data=np.random.rand(args.size, args.size))

# output the dataframe
save_dir = os.path.join(os.getcwd(), args.output_dir)

if not os.path.isdir(save_dir):
    os.makedirs(save_dir)

output_path = os.path.join(save_dir, args.output_fname)

with open(output_path, "w") as f:
    df.to_parquet(path=f)
