# Deep learning framework for Continuous-Time Dynamic Graphs
This is a framework to easlity experiment with Graph Neural Networks (GNNs) in the temporal domain. Specifically, we work in the *continuous-time* setting, i.e., the graph is observed as a stream of events. The framework allows to run robust model selection and assessment leveraging same experimental seeds and data splits, for *reproducible* and *robust* evaluation within the tasks of link prediction and regression. Moreover, our framework allows for distributed (and parallel) model selection.

Currently, we have implemented TGN, TGAT, JODIE, DyRep, and EdgeBank. They can be evaluated on Wikipedia, Reddit, LastFM and MOOC datasets.


---

## Requirements
_Note: we assume Miniconda/Anaconda is installed, otherwise see this [link](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html) for correct installation. The proper Python version is installed during the first step of the following procedure._

Install the required packages and create the environment with create_env script
``` 
./create_env.sh 
```

or create the environment from the yml file
``` 
conda env create -f environment.yml
conda activate ctdg 
```

---

## How to run experiments

### Single machine and Kubernetes cluster
To run the experiments it is important to first set the amount of available resources, i.e., total number of CPUs/GPUs and number of CPUs/GPUs to train each model configuration. We can do this operation in two different ways: 
1. by leveraging environment variables:

```
export NUM_CPUS=<THE NUMBER OF TOTAL AVAILABLE CPUS>
export NUM_GPUS=<THE NUMBER OF TOTAL AVAILABLE GPUS>
export NUM_CPUS_PER_TASK=<THE NUMBER OF CPUS AVAILABLE FOR EACH MODEL CONFIG> 
export NUM_GPUS_PER_TASK=<THE NUMBER/PERCENTAGE OF GPUS AVAILABLE FOR EACH MODEL CONFIG>
```

2. by setting main's arguments:

```
    python main.py --num_cpus <THE NUMBER OF TOTAL AVAILABLE CPUS> --num_gpus <THE NUMBER OF TOTAL AVAILABLE GPUS> --num_cpus_per_task <THE NUMBER OF CPUS AVAILABLE FOR EACH MODEL CONFIG> --num_gpus_per_task <THE NUMBER/PERCENTAGE OF GPUS AVAILABLE FOR EACH MODEL CONFIG>  <OTHER ARGS>
```
Note that `NUM_CPUS` and `NUM_GPUS` are not used while running experiments in a Kubernetes cluster.
We can run the experiments through the command
```
python main.py <YOUR ARGS>
```
Please refer to `run.py` as an example of how to run the experiments, and run `python main.py --help` to know more about main's arguments.

### SLURM cluster
To run the experiment on a SLURM cluster please refer to `run_on_SLURM_cluster.sh`.

--- 

## Add new datasets, models, and negative samplers
- To add new datasets, please refer to `dataset/__init__.py`. _Note: src and dst IDs in the dataset should be in the range [0, num_nodes), e.g.,_ 
```
num_nodes=5
data = TemporalData(src=Tensor([0,1,2,3]),dst=Tensor([1,2,3,4]), t=..., msg=...)
```
- To add new models, please include their implemetation in `models/ctdg_models.py` and the configuration that you want to evaluate in `conf.py`
- To add new negative sampler, please extend the `NegativeSampler` class in `negative_sampler.py` 

