configurations = {
    ##### 0 - BASELINE #####
    "0.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'baseline',
        'experiment_name': '0.1',
        'experiment_args': '{}',
        'dataset_args': { 'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "0.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'baseline',
        'experiment_name': '0.2',
        'experiment_args': '{}',
        'dataset_args': { 'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "0.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'baseline',
        'experiment_name': '0.3',
        'experiment_args': '{}',
        'dataset_args': { 'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },

    ##### 1 - ACTIVATION SHAPING MODULE #####
    #### 1.1 - ONE ASH MODULE ####
    ### 1.1.1 - ASH MODULE AFTER layer1.0.conv1 ###
    "1.1.1.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.1.1',
        'experiment_args': {'module_placement': ['layer1.0.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.1.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.1.2',
        'experiment_args': {'module_placement': ['layer1.0.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.1.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.1.3',
        'experiment_args': {'module_placement': ['layer1.0.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    ### 1.1.2 - ASH MODULE AFTER layer1.0.conv2 ###
    "1.1.2.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.2.1',
        'experiment_args': {'module_placement': ['layer1.0.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.2.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.2.2',
        'experiment_args': {'module_placement': ['layer1.0.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.2.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.2.3',
        'experiment_args': {'module_placement': ['layer1.0.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    ### 1.1.3 - ASH MODULE AFTER layer1.1.conv1 ###
    "1.1.3.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.3.1',
        'experiment_args': {'module_placement': ['layer1.1.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.3.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.3.2',
        'experiment_args': {'module_placement': ['layer1.1.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.3.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.3.3',
        'experiment_args': {'module_placement': ['layer1.1.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    ### 1.1.4 - ASH MODULE AFTER layer1.1.conv2 ###
    "1.1.4.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.4.1',
        'experiment_args': {'module_placement': ['layer1.1.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.4.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.4.2',
        'experiment_args': {'module_placement': ['layer1.1.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.4.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.4.3',
        'experiment_args': {'module_placement': ['layer1.1.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    ### 1.1.5 - ASH MODULE AFTER layer2.0.conv1 ###
    "1.1.5.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.5.1',
        'experiment_args': {'module_placement': ['layer2.0.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.5.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.5.2',
        'experiment_args': {'module_placement': ['layer2.0.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.5.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.5.3',
        'experiment_args': {'module_placement': ['layer2.0.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    ### 1.1.6 - ASH MODULE AFTER layer2.0.conv2 ###
    "1.1.6.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.6.1',
        'experiment_args': {'module_placement': ['layer2.0.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.6.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.6.2',
        'experiment_args': {'module_placement': ['layer2.0.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.6.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.6.3',
        'experiment_args': {'module_placement': ['layer2.0.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    ### 1.1.7 - ASH MODULE AFTER layer2.1.conv1 ###
    "1.1.7.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.7.1',
        'experiment_args': {'module_placement': ['layer2.1.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.7.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.7.2',
        'experiment_args': {'module_placement': ['layer2.1.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.7.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.7.3',
        'experiment_args': {'module_placement': ['layer2.1.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    ### 1.1.8 - ASH MODULE AFTER layer2.1.conv2 ###
    "1.1.8.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.8.1',
        'experiment_args': {'module_placement': ['layer2.1.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.8.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.8.2',
        'experiment_args': {'module_placement': ['layer2.1.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.8.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.8.3',
        'experiment_args': {'module_placement': ['layer2.1.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    ### 1.1.9 - ASH MODULE AFTER layer3.0.conv1 ###
    "1.1.9.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.9.1',
        'experiment_args': {'module_placement': ['layer3.0.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.9.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.9.2',
        'experiment_args': {'module_placement': ['layer3.0.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.9.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.9.3',
        'experiment_args': {'module_placement': ['layer3.0.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    ### 1.1.10 - ASH MODULE AFTER layer3.0.conv2 ###
    "1.1.10.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.10.1',
        'experiment_args': {'module_placement': ['layer3.0.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.10.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.10.2',
        'experiment_args': {'module_placement': ['layer3.0.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.10.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.10.3',
        'experiment_args': {'module_placement': ['layer3.0.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    ### 1.1.11 - ASH MODULE AFTER layer3.1.conv1 ###
    "1.1.11.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.11.1',
        'experiment_args': {'module_placement': ['layer3.1.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.11.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.11.2',
        'experiment_args': {'module_placement': ['layer3.1.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.11.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.11.3',
        'experiment_args': {'module_placement': ['layer3.1.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    ### 1.1.12 - ASH MODULE AFTER layer3.1.conv2 ###
    "1.1.12.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.12.1',
        'experiment_args': {'module_placement': ['layer3.1.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.12.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.12.2',
        'experiment_args': {'module_placement': ['layer3.1.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.12.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.12.3',
        'experiment_args': {'module_placement': ['layer3.1.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    ### 1.1.13 - ASH MODULE AFTER layer4.0.conv1 ###
    "1.1.13.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.13.1',
        'experiment_args': {'module_placement': ['layer4.0.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.13.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.13.2',
        'experiment_args': {'module_placement': ['layer4.0.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.13.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.13.3',
        'experiment_args': {'module_placement': ['layer4.0.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    ### 1.1.14 - ASH MODULE AFTER layer4.0.conv2 ###
    "1.1.14.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.14.1',
        'experiment_args': {'module_placement': ['layer4.0.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.14.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.14.2',
        'experiment_args': {'module_placement': ['layer4.0.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.14.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.14.3',
        'experiment_args': {'module_placement': ['layer4.0.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    ### 1.1.15 - ASH MODULE AFTER layer4.1.conv1 ###
    "1.1.15.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.15.1',
        'experiment_args': {'module_placement': ['layer4.1.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.15.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.15.2',
        'experiment_args': {'module_placement': ['layer4.1.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.15.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.15.3',
        'experiment_args': {'module_placement': ['layer4.1.conv1'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    ### 1.1.16 - ASH MODULE AFTER layer4.1.conv2 ###
    "1.1.16.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.16.1',
        'experiment_args': {'module_placement': ['layer4.1.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.16.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.16.2',
        'experiment_args': {'module_placement': ['layer4.1.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.16.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': '1.1.16.3',
        'experiment_args': {'module_placement': ['layer4.1.conv2'], 'mask_out_ratio': 0.5},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },

    #### 1.2 - TWO ASH MODULES ####
}
