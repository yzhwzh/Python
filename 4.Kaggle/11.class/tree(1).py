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

    def fit(self,train):
        self.estimator = self.construct_tree(train,label,depth_left=self.max_depth)

    def construct_tree(self,train,label,depth_left):
        if depth_left==0 or len(train)<self.min_sample_split:
            return TreeNode(is_leaf=True,score=self.calculate_score(label))

        feature,threshold,gain=self.find_best_feature_threshold_and_gain(train,label)

        if gain<=self.gamma:
            return TreeNode(is_leaf=True,score=self.calculate_score(label))

        index=train[:,feature]<threshold
        left=self.construct_tree(train[index],label[index],depth_left-1)
        right=self.construct_tree(train[~index],label[~index],depth_left-1)
        return TreeNode(feature=feature,threshold=threshold,left=left,right=right)


    # 输入叶子节点内数据的标签，返回该节点的预测值
    def calculate_score(self,label):
        return score
    
    # 输入训练数据和label，返回最佳分裂特征、最佳分裂点、增益
    def find_best_feature_threshold_and_gain(self,train,label):
        return best_feature,best_threshold,best_gain