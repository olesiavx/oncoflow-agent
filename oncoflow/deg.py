#tiny differential expression analysis
import numpy as np
import pandas as pd

def run_deg(expr, clin):
    #this computes mean difference in expression between two groups defined in clinical data
    if "status" not in clin.columns:
        return None
    
    group1 = expr.loc[:, clin["status"] == 0].mean(axis=1)
    group2 = expr.loc[:, clin["status"] == 1].mean(axis=1)

    fold_change = group2 - group1
    fc_df = pd.DataFrame({"gene": expr.index, "fold_change": fold_change})
    return fc_df.sort_values("fold_change", ascending=False)
