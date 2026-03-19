# BottleneckOracle

> Predicting and explaining bottlenecks in LLM training jobs using heterogeneous graph neural networks.

## What this project does

When you train a large language model across many GPUs, the training run produces an **execution trace** — a detailed log of every operation, how long it took, and what depended on what. This project converts those traces into graphs and trains a GNN to:
- Predict step time and per-node slack (how much delay each operation can absorb)
- Identify which nodes are causally responsible for slowdowns
- Suggest optimizations via a GraphRAG loop (LLM + GNN validation)

## Team

| Person | Role | Owns |
|--------|------|------|
| Preetham V J | Graph Pipeline Dev | `src/graph_pipeline/`, `data/` |
| Archita Jain | ML Researcher | `src/models/`, `src/training/` |
| Aaron Thomas Mathew | Systems Architect | `src/systems/`, `src/llm/` |

## Repo structure

```
BottleneckOracle/
├── data/
│   ├── raw/          # Picotron trace files (.json) 
│   └── graphs/       # Processed PyG HeteroData (.pt) 
├── src/
│   ├── graph_pipeline/
│   │   ├── parser.py       # Chakra trace → NetworkX DAG
│   │   ├── features.py     # Node/edge feature engineering
│   │   └── directed_mp.py  # Directed message passing variant
│   ├── models/
│   │   ├── hetero_gat.py   # HeteroGAT (bidirectional + directed variants)
│   │   └── baselines.py    # MLP, XGBoost, 1F1B formula
│   ├── training/
│   │   ├── train.py        # Training loop (multi-task: step time + slack)
│   │   └── eval.py         # Spearman ρ, ΔT accuracy, OOD splits
│   ├── systems/
│   │   ├── picotron_hook.py  # Picotron instrumentation + delay injection
│   │   └── whatif.py         # Perturbation harness (edit node → predict ΔT)
│   └── llm/
│       └── graphrag.py       # Causal subgraph → LLM → optimizer suggestions
├── notebooks/
│   └── eda.ipynb         # Exploratory data analysis
├── paper/                # LaTeX source
├── interface.py          # PyG HeteroData contract (read this before week 4)
├── config.yaml           # Hyperparameters and dataset paths
├── requirements.txt
└── README.md
```

## Quickstart

```bash
pip install -r requirements.txt

# Step 1: Parse a trace into a graph
python src/graph_pipeline/parser.py --input data/raw/trace.json --output data/graphs/

# Step 2: Train the GNN
python src/training/train.py --config config.yaml

# Step 3: Run evaluation
python src/training/eval.py --checkpoint checkpoints/best.pt


Node types: `compute`, `network`
Edge types: `('compute', 'depends_on', 'compute')`, `('compute', 'triggers', 'network')`


## What we defer to future work

- Hardware tier nodes (GPU util, HBM BW, SM occupancy) — needs ASTRA-Sim
- Full NCM / do-calculus causal overlay
- LOGIC NL explainer
- LoRA cross-hardware adapter
