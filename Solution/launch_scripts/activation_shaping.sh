network_type=${1}
target_domain=${2}

echo "Use random.sh, setting the desired module_placement."
exit

python main.py \
--experiment=${network_type} \
--experiment_name=${network_type}/${target_domain}/ \
--dataset_args="{ 'text_root': 'data', 'images_root': 'data/kfold/PACS', 'source_domain': 'art_painting', 'target_domain': '${target_domain}' }" \
--batch_size=128 \
--num_workers=5 \
--grad_accum_steps=1
