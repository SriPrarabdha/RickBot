# Code run on a Kaggle notebook

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from simplet5 import SimpleT5

df = pd.read_csv("../input/rickmorty-scripts/RickAndMortyScripts.csv" , low_memory = False)

context_x = []
response_y = []
for i in range(1 , 1905):
  if df['name'][i] == 'Rick' :
    context_x.append(df['line'][i-1])
    response_y.append(df['line'][i])

col = [ 'source_text' , 'target_text']

data = pd.DataFrame(list(zip(context_x, response_y)),
               columns =['source_text', 'target_text'])

train_df , test_df = train_test_split(data , test_size = .2)

model = SimpleT5()

model.from_pretrained("t5","t5-base")

model.train(train_df=train_df, # pandas dataframe with 2 columns: source_text & target_text
            eval_df=test_df, # pandas dataframe with 2 columns: source_text & target_text
            source_max_token_len = 256, 
            target_max_token_len = 256,
            batch_size = 8,
            max_epochs = 12,
            use_gpu = True,
            outputdir = "outputs",
            
            )

model.load_model("t5" , "/kaggle/working/outputs/simplet5-epoch-11-train-loss-1.6434-val-loss-4.2524" , use_gpu=True)