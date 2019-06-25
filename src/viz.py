import numpy as np
import matplotlib.pyplot as plt


def plot_feature_importance(imp_df, has_std=False):
    y_pos = np.arange(imp_df.shape[0])
    plt.figure(figsize=(15, 7))
    plt.title('Feature Importance plot (Higher is better)')
    if has_std:
        ax = plt.barh(y_pos, imp_df['score'], xerr=1.96 * imp_df['std'])
    else:
        ax = plt.barh(y_pos, imp_df['score'])
    plt.xlabel('Score')
    plt.ylabel('Features')
    plt.yticks(ticks=y_pos, labels=imp_df['feature'])
    return ax
