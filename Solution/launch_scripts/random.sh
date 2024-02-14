target_domain=${1}
mask_out_ratio=${2}

python main.py \
--experiment=random \
--experiment_name=random/${target_domain}/ \
--experiment_args="{'module_placement': ['layer2.1.conv2'], 'mask_out_ratio': ${mask_out_ratio}}" \
--dataset_args="{'root': 'data/PACS', 'source_domain': 'art_painting', 'target_domain': '${target_domain}'}" \
--batch_size=128 \
--num_workers=5 \
--grad_accum_steps=1
