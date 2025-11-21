#generic Xena unwrapper, loads tab-delimited tables into pandas dataframes. works for .txt,
# .tsv, .csv, .gz if tab-delimited

from pathlib import Path
import pandas as pd


def load_xena_table(path, index_col=None):

    path = Path(path)

    df = pd.read_table(
        path,
        sep="\t",
        index_col=index_col,
        comment="#",          # Xena adds comments at top
        low_memory=False,     # big files → avoid dtype guessing mess
    )
    return df

#example, specialised functions for the sample data in data/raw. all of the data is from xena. 
def load_brca_expression(path="data/raw/HiSeqV2-2.tsv"):
    return load_xena_table(path, index_col=0)


def load_brca_clinical(path="data/raw/TCGA.BRCA.sampleMap-BRCA_clinicalMatrix.tsv"):
    return load_xena_table(path, index_col=0)


def load_brca_survival(path="data/raw/BRCA_survival.csv"):
    df = pd.read_csv(path)
    return df

#loading expression + clinical csvs 
import pandas as pd

def load_expression(path):
    return pd.read_csv(path, index_col=0)

def load_clinical(path):
    return pd.read_csv(path, index_col=0)

#moving the downloads from xena configured to csvs into data/raw
#from oncoflow.loaders import load_brca_expression, load_brca_clinical
#expr = load_brca_expression()
#clin = load_brca_clinical()
#print(expr.shape, clin.shape)
