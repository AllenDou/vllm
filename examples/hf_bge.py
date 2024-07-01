
from FlagEmbedding import FlagReranker
reranker = FlagReranker('BAAI/bge-reranker-base', use_fp16=True) # Setting use_fp16 to True speeds up computation with a slight performance degradation
score = reranker.compute_score([('hello world', 'nice to meet you'), ("yes","no")])
print(score)
del reranker

from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSequenceClassification, is_torch_npu_available
from typing import Union, List, Tuple, Any
import torch
from transformers import XLMRobertaTokenizerFast

model_name_or_path = "BAAI/bge-reranker-base"
cache_dir = None
max_length = 512

sentence_pairs: Union[List[Tuple[str, str]], Tuple[str, str]] = \
    [("hello world", "nice to meet you"), ("yes", "no")]
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, cache_dir=cache_dir)
# XLMRobertaForSequenceClassification
model = AutoModelForSequenceClassification.from_pretrained(model_name_or_path, cache_dir=cache_dir)
model = model.to("cuda")
model.eval()
import pdb; pdb.set_trace()

#tokenizer.encode()
inputs = tokenizer(
    sentence_pairs,
    padding=True,
    truncation=True,
    return_tensors='pt',
    max_length=max_length,
).to("cuda")

#inputs = tokenizer.encode(
#    sentence_pairs,
#    padding=True,
#    truncation=True,
#    return_tensors='pt',
#    max_length=max_length,
#).to("cuda")

all_scores = []
with torch.no_grad():
    scores = model(**inputs, return_dict=True).logits.view(-1, ).float()
    all_scores.extend(scores.cpu().numpy().tolist())
    normalize = False
    #if normalize:
    #    all_scores = [sigmoid(score) for score in all_scores]
