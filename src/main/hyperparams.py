import os
hyperparameter_defaults = dict(
    dropout = 0.1,
    batch_size = 512,
    test_batch_size=128,
    lr = 0.001,
    momentum = 0.9,
    no_cuda = False,
    seed = 1,
    epochs = 24,
    bias = False,
    sched_lr_gamma = 0.5,
    sched_lr_step= 1,
    start_lr = 0,
    weight_decay=0.0000,
    lr_decay_threshold=0.0,
    factor=0.0,
    project="news5",
    ocp_max_lr=0.5
    )

def print_hyperparams():
    for key,value in hyperparameter_defaults.items():
        print('%20s : %s ' % (key, value))

def get_hyperparam(key_item):
    return hyperparameter_defaults[key_item]

def set_hyperparam(params_dict):
    for key_item, val_item in params_dict.items(): 
        hyperparameter_defaults[key_item] = val_item
