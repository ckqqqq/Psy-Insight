from typing import List
import evaluate
import jieba
import nltk
class Bleu():
    def __init__(self):
        self.model = nltk.translate.bleu_score.sentence_bleu
        self.smoothing_func = nltk.translate.bleu_score.SmoothingFunction().method1
    def calc(self,hyps:list,ref:list,ngram_list:List[int]):
        if len(hyps)>1 or len(ref)>1:
            raise ValueError()
        else:
            ref = ' '.join(jieba.cut(ref[0]))
            hyps = ' '.join(jieba.cut(hyps[0]))
            # 获取 n 的值
            result={}
            for ngram in ngram_list:
                n = ngram  # 如果没有传递 n，则使用默认的 ngram
                weights = [1 / n] * n  # 根据传入的 n 计算权重
                ref_list=[ref.split()]
                blue_n = self.model(ref_list, hyps.split(), weights=weights, smoothing_function=self.smoothing_func)
                result['blue-'+str(n)]=blue_n
            return result
    def note():
        """
        https://blog.csdn.net/a14285700/article/details/137247574
        weights_1 = (1.0, 0, 0, 0)
    weights_2 = (0.5, 0.5, 0, 0)
    weights_3 = (0.33, 0.33, 0.33, 0)
        """
bleu=Bleu()
print(bleu.calc(["Nice to Meet you."],["Hi, you are so beautiful !"],[1,2,3,4]))