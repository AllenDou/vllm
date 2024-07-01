import argparse
import os
import subprocess

import torch
from PIL import Image

from typing import Union, List, Tuple, Any

from vllm import LLM
from vllm.multimodal.image import ImageFeatureData, ImagePixelData, BgeData
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSequenceClassification, is_torch_npu_available


def run():
    model_name_or_path = "BAAI/bge-reranker-base"
    cache_dir = None
    max_length = 512
    import pdb; pdb.set_trace()
    llm = LLM(
        model=model_name_or_path,
        #image_input_type="pixel_values",
        #image_token_id=32000,
        #image_input_shape="1,3,336,336",
        #image_feature_size=576,
        #disable_image_processor=disable_image_processor,
    )

    prompt = "this is a Bge reranker call."
    sentence_pairs: Union[List[Tuple[str, str]], Tuple[str, str]] = \
        [("hello world", "nice to meet you"), ("yes", "no")]
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path,
                                              cache_dir=cache_dir)
    inputs = tokenizer(
        sentence_pairs,
        padding=True,
        truncation=True,
        return_tensors='pt',
        max_length=max_length,
    ).to("cuda")

    outputs = llm.generate({
        "prompt": prompt,
        #"multi_modal_data": ImagePixelData(image),
        "multi_modal_data": BgeData(inputs),
    })

    for o in outputs:
        generated_text = o.outputs[0].text
        print(generated_text)


def main(args):
    run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Demo on BGE reranker")
    #parser.add_argument("--type",
    #                    type=str,
    #                    choices=["pixel_values", "image_features"],
    #                    default="pixel_values",
    #                    help="image input type")
    args = parser.parse_args()

    main(args)
