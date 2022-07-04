import numpy as np

class RoundRobinSearch:
    """
    ディクショナリから総当たりで新たな辞書を生成し、リストにして返す「search()」メソッドを使用する。
    """
    def _recur(self,keys,props,prop_use,resultSet):
        key = keys[0] #現在参照中のキー
        row = props[key] #現在参照中のリスト
                
        for li_idx in range(len(row)): #リストの探索
            prop_use[key] = row[li_idx] #値を格納
            if len(keys) == 1: #最後のキーの値が決まったとき
                resultSet.append(prop_use.copy()) #prop_useは参照値のため、コピーを追加する必要あり
                continue
            resultSet = self._recur(keys[1:],props,prop_use,resultSet)
        return resultSet

    def search(self,props):
        """
        Parameters
        -----------------------
        props : dict
            生成元の辞書
        
        Returns
        -----------------------
        resultSet : list
            辞書を複数含んだリスト
        """

        prop_use = {}
        resultSet = []
        keys = [k for k in props.keys()] #キー一覧
        
        print(">")
        print(f"props keys ==> {keys}")
        print(">")
            
        return self._recur(keys,props,prop_use,resultSet)