confs = {
    # ----- Baseline -----
    "0.1.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'baseline',
        'experiment_name': 'baseline/cartoon/',
        'experiment_args': '{}',
        'dataset_args': { 'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "0.1.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'baseline',
        'experiment_name': 'baseline/sketch/',
        'experiment_args': '{}',
        'dataset_args': { 'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "0.1.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'baseline',
        'experiment_name': 'baseline/photo/',
        'experiment_args': '{}',
        'dataset_args': { 'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    # ----- Activation Shaping module -----
    # --- ASH module after last convolutional layer ---
    "1.1.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': 'random/after_last_conv/cartoon/',
        'experiment_args': {'module_placement': ['layer4.1.conv2'], 'mask_out_ratio': 0.1},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.2" : { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': 'random/after_last_conv/sketch/',
        'experiment_args': {'module_placement': ['layer4.1.conv2'], 'mask_out_ratio': 0.1},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "1.1.3" : { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': 'random/after_last_conv/photo/',
        'experiment_args': {'module_placement': ['layer4.1.conv2'], 'mask_out_ratio': 0.1},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    # --- ASH module after each convolutional layer ---
    "1.2.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': 'random/after_each_conv/cartoon/',
        'experiment_args': {'module_placement': ['layer1.0.conv1', 'layer1.0.conv2', 'layer1.1.conv1', 'layer1.1.conv2', 'layer2.0.conv1', 'layer2.0.conv2', 'layer2.1.conv1', 'layer2.1.conv2', 'layer3.0.conv1', 'layer3.0.conv2', 'layer3.1.conv1', 'layer3.1.conv2', 'layer4.0.conv1', 'layer4.0.conv2', 'layer4.1.conv1', 'layer4.1.conv2'], 'mask_out_ratio': 0.1},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    # --- ASH module after last convolutional layer ---
    "1.3.1" : { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': 'random/every_three_conv/cartoon/',
        'experiment_args': {'module_placement': ['layer1.0.conv1', 'layer1.1.conv2', 'layer2.1.conv1', 'layer3.0.conv2', 'layer4.0.conv1', 'layer4.1.conv2'], 'mask_out_ratio': 0.1},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    # ----- Random Activation Maps -----
    # --- mor = 0.4, mp = layer4.1.conv2 ---
    "2.1.1": { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': 'random/case1/cartoon/',
        'experiment_args': {'module_placement': ['layer4.1.conv2'], 'mask_out_ratio': 0.4},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "2.1.2": { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': 'random/case1/sketch/',
        'experiment_args': {'module_placement': ['layer4.1.conv2'], 'mask_out_ratio': 0.4},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "2.1.3": { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': 'random/case1/photo/',
        'experiment_args': {'module_placement': ['layer4.1.conv2'], 'mask_out_ratio': 0.4},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    # --- mor = 0.55, mp = layer4.1.conv2 ---
    "2.2.1": { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': 'random/case1/cartoon/',
        'experiment_args': {'module_placement': ['layer4.1.conv2'], 'mask_out_ratio': 0.55},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "2.2.2": { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': 'random/case1/sketch/',
        'experiment_args': {'module_placement': ['layer4.1.conv2'], 'mask_out_ratio': 0.55},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "2.2.3": { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': 'random/case1/photo/',
        'experiment_args': {'module_placement': ['layer4.1.conv2'], 'mask_out_ratio': 0.55},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    # --- mor = 0.75, mp = layer4.1.conv2 ---
    "2.3.1": { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': 'random/case1/cartoon/',
        'experiment_args': {'module_placement': ['layer4.1.conv2'], 'mask_out_ratio': 0.75},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "2.3.2": { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': 'random/case1/sketch/',
        'experiment_args': {'module_placement': ['layer4.1.conv2'], 'mask_out_ratio': 0.75},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "2.3.3": { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'random',
        'experiment_name': 'random/case1/photo/',
        'experiment_args': {'module_placement': ['layer4.1.conv2'], 'mask_out_ratio': 0.75},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    # ----- Adapting Activation Maps across Domains -----
    # --- mp = layer2.1.conv2 ---
    "3.1.1": { # Art Painting -> Cartoon
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'domain_adaptation',
        'experiment_name': 'domain_adaptation/cartoon/',
        'experiment_args': {'module_placement': ['layer2.1.conv2']},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'cartoon' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "3.1.2": { # Art Painting -> Sketch
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'domain_adaptation',
        'experiment_name': 'domain_adaptation/sketch/',
        'experiment_args': {'module_placement': ['layer2.1.conv2']},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'sketch' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
    "3.1.3": { # Art Painting -> Photo
        'seed': 0,
        'test_only': False,
        'cpu': False,
        'experiment': 'domain_adaptation',
        'experiment_name': 'domain_adaptation/photo/',
        'experiment_args': {'module_placement': ['layer2.1.conv2']},
        'dataset_args': {'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': 'photo' },
        'batch_size': 128,
        'epochs': 30,
        'num_workers': 5,
        'grad_accum_steps': 1
    },
}