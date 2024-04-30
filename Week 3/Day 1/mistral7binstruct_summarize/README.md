---
license: apache-2.0
library_name: peft
tags:
- trl
- sft
- generated_from_trainer
base_model: mistralai/Mistral-7B-Instruct-v0.2
datasets:
- generator
model-index:
- name: mistral7binstruct_summarize
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mistral7binstruct_summarize

This model is a fine-tuned version of [mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) on the generator dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4683

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: constant
- lr_scheduler_warmup_steps: 0.03
- training_steps: 50

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 1.681         | 0.2174 | 25   | 1.5701          |
| 1.5158        | 0.4348 | 50   | 1.4683          |


### Framework versions

- PEFT 0.10.0
- Transformers 4.40.1
- Pytorch 2.2.2+cu121
- Datasets 2.19.0
- Tokenizers 0.19.1