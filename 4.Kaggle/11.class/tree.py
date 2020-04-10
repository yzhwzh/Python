class TreeNode(object):
    def __init__(self,
        is_leaf=False,score=None,
        feature=None,threshold=None,left=None,right=None):
        self.is_leaf=is_leaf
        self.score=score
        self.feature=feature
        self.threshold=threshold
        self.left=left
        self.right=right
        
class Tree(object):
    def __init__(self,estimator=None,max_depth=3,min_sample_split=10,gamma=0):
        self.estimator = estimator
        self.max_depth=max_depth
        self.min_sample_split=min_sample_split
        self.gamma=gamma
        
    def predict_single(self,treenode,test):
        if treenode.is_leaf:
            return treenode.score
        else:
            if test[treenode.feature]<treenode.threshold:
                return self.predict_single(treenode.left,test)
            else:
                return self.predict_single(treenode.right,test)
            
    def predict(self,test):
        result = []
        for i in test:
            result.append(self.predict_single(self.estimator,i))
        return result