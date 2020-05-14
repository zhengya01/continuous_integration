#!/usr/bin/env python
"""
this is bert args
"""

pretrain = {
    "use_cuda": [True],
    "weight_sharing": [True, False],
    "batch_size": [4096],
    "data_dir": ["./args_test_data/train/"],
    "validation_set_dir": ["./args_test_data/validation/"],
    "bert_config_path":
    ["args_test_model/chinese_L-12_H-768_A-12/bert_config.json"],
    "vocab_path": ["args_test_model/chinese_L-12_H-768_A-12/vocab.txt"],
    "generate_neg_sample": [True, False],
    "checkpoints": ["output"],
    "save_steps": [100],
    "learning_rate": [0.0001],
    "weight_decay": [0.01],
    "max_seq_len": [512],
    "skip_steps": [10],
    "validation_steps": [10],
    "num_iteration_per_drop_scope": [10],
    "use_fp16": [False, True],
    "verbose": [True],
    "is_distributed": [False],
    "epoch": [1],
}

finetune_cls = {
    "bert_config_path":
    ["args_test_model/chinese_L-12_H-768_A-12/bert_config.json"],
    "init_checkpoint": ["args_test_model/chinese_L-12_H-768_A-12/", None],
    "init_pretraining_params":
    ["args_test_model/chinese_L-12_H-768_A-12/params", "None"],
    "checkpoints": ["args_test_output"],
    "verbose": [False, True],
    "vocab_path": ["args_test_model/chinese_L-12_H-768_A-12/vocab.txt"],
    "do_lower_case": [True, False],
    "random_seed": [0, 100],
    "shuffle": [True, False],
    "task_name": ["XNLI"],
    "do_train": [True],
    "do_val": [False, True],
    "do_test": [False, True],
    "epoch": [1],
    "lr_scheduler": ["linear_warmup_decay", "noam_decay"],
    "use_fp16": [False, True],
    "data_dir": ["./args_test_data/finetune/XNLI-MT-1.0/"],
    "batch_size": [32, 128],
    "max_seq_len": [128, 512],
    "in_tokens": [False],
    "use_cuda": [True],
    "use_fast_executor": [False, True],
    "num_iteration_per_drop_scope": [1, 100],
    "save_steps": [1000],
    "weight_decay": [0.01],
    "warmup_proportion": [0.1],
    "validation_steps": [100],
    "skip_steps": [10],
    "num_iteration_per_drop_scope": [10],
    "verbose": [True],
}

finetune_squad = {
    "use_cuda": [True],
    "batch_size": [12],
    "in_tokens": [False],
    "init_pretraining_params":
    ["args_test_model/chinese_L-12_H-768_A-12/params"],
    "checkpoints": ["args_test_output"],
    "vocab_path": ["args_test_model/chinese_L-12_H-768_A-12/vocab.txt"],
    "do_train": [True],
    "do_predict": [True],
    "save_steps": [100],
    "warmup_proportion": [0.1],
    "weight_decay": [0.01],
    "epoch": [1],
    "max_seq_len": [512],
    "bert_config_path":
    ["args_test_model/chinese_L-12_H-768_A-12/bert_config.json"],
    "predict_file": ["args_test_data/finetune/SQuAD1.1/dev-v1.1.json"],
    "do_lower_case": [True, False],
    "doc_stride": [128],
    "train_file": ["args_test_data/finetune/SQuAD1.1/train-v1.1.json"],
    "learning_rate": [0.00003],
    "lr_scheduler": ["linear_warmup_decay", "noam_decay"],
    "skip_steps": [10],
    "init_checkpoint": ["args_test_model/chinese_L-12_H-768_A-12/", None],
    "verbose": [False, True],
    "random_seed": [0, 100],
    "use_fp16": [False, True],
    "max_answer_length": [30],
    "batch_size": [32],
    "use_fast_executor": [False, True],
    "num_iteration_per_drop_scope": [1],
}
