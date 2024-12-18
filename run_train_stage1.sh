 accelerate launch --gpu_ids 1 --use_deepspeed --num_processes 1 \
   --deepspeed_config_file zero_stage2_config.json \
   --deepspeed_multinode_launcher standard \
   train_stage1.py