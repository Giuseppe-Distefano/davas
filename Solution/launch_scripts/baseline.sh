target_domain=${1}

python main.py \
--experiment=baseline \
--experiment_name=baseline/${target_domain}/ \
--dataset_args="{ 'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': '${target_domain}' }" \
--batch_size=128 \
--num_workers=5 \
--grad_accum_steps=1