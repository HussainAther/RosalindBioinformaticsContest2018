from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

def sample_loss(params):
    C = params[0]
    gamma = params[1]

    # Sample C and gamma on the log-uniform scale
    model = SVC(C=10 ** C, gamma=10 ** gamma, random_state=12345)

    # Sample parameters on a log scale
    return cross_val_score(model=model, X=data, y=target, scoring='roc_auc', cv=3).mean()
