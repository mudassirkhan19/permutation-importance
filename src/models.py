import eli5
import pandas as pd
from eli5.formatters.as_dataframe import format_as_dataframe
from eli5.sklearn import PermutationImportance


def permutation_importance_df(model, X, y):
    perm = PermutationImportance(model, random_state=42).fit(X, y)
    expl = eli5.explain_weights(perm, feature_names=X.columns.tolist())
    imp_df = format_as_dataframe(expl).sort_values(by='weight', ascending=True).rename(columns={'weight': 'score'})
    return imp_df


def gini_importance_df(model, columns):
    feature_imp_list = []
    for feature in zip(columns, model.feature_importances_):
        feature_imp_list.append(feature)
    fi_gini = pd.DataFrame(feature_imp_list, columns=['feature', 'score']).sort_values(by='score')
    return fi_gini