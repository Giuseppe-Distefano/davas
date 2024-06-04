k_values=(0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40 0.45 0.50 0.55 0.60 0.65 0.70 0.75 0.80 0.85 0.90 0.95 1.00)

for k in "${k_values[@]}"
do
  echo "k: $k"
  rm -rf record/domain_adaptation
  ./launch_scripts/domain_adaptation_top_k.sh photo 'layer4.1.conv2' "$k, $k, $k, $k"
  acc="$(tail -1 record/domain_adaptation/photo/log.txt)"
  echo "${k} : ${acc}" >> ./launch_scripts/da_top_k_photo_layer4.1.conv2_output.txt
done

