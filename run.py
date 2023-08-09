import os

folder='.'
num_runs=5
epochs=1000
patience=50
cluster=True
log=True
cpus_per_task=2
gpus_per_task=0.

 
for data in ['Wikipedia', 'Reddit', "LastFM"]:
    for model in ['DyRep', 'JODIE', 'TGAT', 'TGN', 'EdgeBank']:
        if model == 'EdgeBank':
            num_runs=1
            epochs=1
            
        parallelism =  20

        cmd = (f"python3 -u main.py --data_dir {folder}/DATA --data_name {data} --save_dir {folder}/RESULTS "
               f"--model {model} --num_runs {num_runs} --epochs {epochs} --patience {patience} "
               f"--num_cpus_per_task {cpus_per_task} --num_gpus_per_task {gpus_per_task} "
               f"--parallelism {parallelism} "
               f"{'--cluster' if cluster else ''} --verbose {'--log' if log else ''} "
               f"> {folder}/out_same_dim4_{model}_{data} 2> {folder}/err_same_dim4_{model}_{data}")
        print('Running:', cmd)
        os.system(cmd)
