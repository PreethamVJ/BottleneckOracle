# BottleneckOracle Repository Structure

**Overview:** A research project focused on predicting and explaining bottlenecks in LLM training jobs using heterogeneous graph neural networks. The project converts training execution traces into graphs and trains GNNs to predict step times, identify critical nodes, and suggest optimizations.

---

## 📁 Repository Structure

```
BottleneckOracle/
├── README.md                          # Main project documentation
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Version control exclusions
├── patch_nb03.py                      # Notebook patching utility
├── REPOSITORY_STRUCTURE.md            # This file
├── data/                              # Data storage
│   ├── graphs/.gitkeep               # Processed PyG HeteroData files (.pt)
│   └── raw/.gitkeep                  # Raw trace files (.json)
├── src/                              # Source code (planned structure)
│   ├── graph_pipeline/.gitkeep       # Chakra trace → NetworkX DAG
│   ├── models/.gitkeep              # HeteroGAT and baseline models
│   ├── training/.gitkeep            # Training and evaluation scripts
│   ├── systems/.gitkeep             # Picotron instrumentation tools
│   └── llm/.gitkeep                 # GraphRAG integration utilities
├── notebooks/                        # Research implementation
│   ├── 01_trace_generation_ipynb.ipynb
│   ├── 02-trace-generation-fixed.ipynb
│   ├── 03_heterogat_fixed.ipynb
│   ├── 04_timing_based_dag.ipynb
│   ├── model_1f1b.ipynb
│   └── Citation.ris
└── paper/                            # Academic paper documentation
    └── .gitkeep
```

---

## 📄 Root Level Files

### **README.md**
**Purpose:** Main project documentation and quickstart guide  
**Contents:**
- Project description and goals
- Team structure and ownership
- Repository structure overview
- Quickstart commands
- Node and edge type definitions
- Future work roadmap

### **requirements.txt**
**Purpose:** Python dependencies specification  
**Key Dependencies:**
- **Deep Learning:** `torch`, `torch-geometric`
- **Graph Processing:** `networkx`
- **Data Science:** `numpy`, `pandas`, `scikit-learn`, `xgboost`
- **Visualization:** `matplotlib`
- **Utilities:** `scipy`, `tqdm`, `pyyaml`

### **.gitignore**
**Purpose:** Version control exclusions  
**Excludes:**
- Data directories (`data/raw/`, `data/graphs/`)
- Cache and build artifacts (`__pycache__/`, `*.pyc`)
- Environment files (`.env`)
- Model checkpoints (`*.pt`, `*.pth`)
- Virtual environments (`venv/`)

### **patch_nb03.py**
**Purpose:** Utility script for patching notebook 03  
**Functionality:**
- Updates imports from `huggingface_hub` to use `snapshot_download`
- Modifies graph-loading code to use correct repository ID
- Applies fixes for notebook compatibility issues

---

## 🔧 Source Code Structure (`src/`)

**Status:** Currently contains placeholder files (.gitkeep) - planned modular structure  
**Note:** Actual implementation is in the notebooks directory

### **src/graph_pipeline/** (Planned)
**Purpose:** Chakra trace → NetworkX DAG conversion pipeline  
**Intended Functionality:**
- Parse Chakra execution traces
- Build directed acyclic graphs
- Feature engineering and preprocessing

### **src/models/** (Planned)
**Purpose:** HeteroGAT and baseline model implementations  
**Intended Functionality:**
- Heterogeneous GNN architectures
- Multi-task learning frameworks
- Baseline comparison models

### **src/training/** (Planned)
**Purpose:** Training and evaluation scripts  
**Intended Functionality:**
- Model training loops
- Evaluation metrics
- Experiment logging

### **src/systems/** (Planned)
**Purpose:** Picotron instrumentation tools  
**Intended Functionality:**
- Production trace collection
- Performance monitoring
- Real-time analysis

### **src/llm/** (Planned)
**Purpose:** GraphRAG integration utilities  
**Intended Functionality:**
- LLM-based optimization suggestions
- Graph retrieval augmented generation
- Natural language explanations

---

## 📓 Notebooks (`notebooks/`)

### **01_trace_generation_ipynb.ipynb**
**Purpose:** Proof-of-concept trace generation pipeline  
**Key Features:**
- Generates synthetic transformer traces using PyTorch Profiler
- Parses Chrome traces into NetworkX graphs
- Implements basic feature engineering and critical path analysis
- Converts to PyTorch Geometric HeteroData format
- Generates 501 synthetic graphs across 3 model configurations  
**Output:** Initial dataset with basic graph structure

### **02-trace-generation-fixed.ipynb**
**Purpose:** Enhanced trace generation with HuggingFace integration  
**Improvements over v1:**
- Fixes graph edge construction timing logic
- Implements proper multi-task head (node + graph level)
- Adds batch upload to HuggingFace datasets
- Implements directed vs bidirectional GAT variants
- Includes comprehensive validation checks  
**Output:** Production-ready dataset with proper labels

### **03_heterogat_fixed.ipynb**
**Purpose:** Core HeteroGAT model implementation  
**Key Features:**
- Two-layer heterogeneous GNN with GAT convolutions
- Multi-task learning (node criticality + step time prediction)
- Bidirectional vs directed message passing variants
- Comprehensive evaluation with baselines
- Acceptance criteria testing  
**Models:** HeteroGAT with attention mechanisms

### **04_timing_based_dag.ipynb**
**Purpose:** Realistic DAG construction based on timing constraints  
**Key Innovation:**
- Timing-based edge creation (non-overlapping ops only)
- Generates genuine parallelism in graphs
- Improved critical path labeling
- 501 graphs with healthy variance in critical node fractions  
**Output:** More realistic parallel execution graphs

### **model_1f1b.ipynb**
**Purpose:** 1F1B analytic baseline comparison  
**Functionality:**
- Implements 1F1B formula (sum of compute node durations)
- MLP baseline implementation
- Train/validation/test split management
- Error analysis and comparison  
**Baselines:** Analytical formulas and simple MLP

### **Citation.ris**
**Purpose:** Academic reference file  
**Content:** Citation for electrocardiogram standardization paper (placeholder/example)

---

## 💾 Data Directory (`data/`)

**Status:** Contains placeholder files - actual data hosted on HuggingFace

### **data/graphs/.gitkeep**
**Purpose:** Placeholder for processed PyG HeteroData files (.pt)  
**Content:** Graph objects ready for GNN training

### **data/raw/.gitkeep**
**Purpose:** Placeholder for raw trace files (.json)  
**Content:** Chrome trace format execution traces

**Dataset Information:**
- **Size:** 501 synthetic training traces
- **Configurations:** 3 transformer model sizes (tiny, small, medium)
- **Hosted:** HuggingFace dataset `preethamvj/bottleneck-oracle-graphs`
- **Split:** 70% train, 15% validation, 15% test

---

## 📝 Paper Directory (`paper/`)

**Status:** Currently contains only placeholder file  
**Purpose:** Academic paper documentation and LaTeX sources

---

## 🔬 Technical Architecture

### **Node Types**
- **`compute`:** Neural network operations (matmul, attention, etc.)
- **`network`:** Communication operations (allreduce, comm, etc.)

### **Edge Types**
- **`('compute', 'depends_on', 'compute')`:** Sequential dependencies
- **`('compute', 'sends_to', 'network')`:** Compute to communication
- **`('network', 'feeds', 'compute')`:** Communication to compute

### **Features**
- **`duration_ms`:** Operation duration
- **`compute_ratio`:** Duration relative to total time
- **`norm_duration`:** Normalized duration
- **`is_critical`:** Binary label from critical path analysis

### **Model Architecture**
- **Input:** Heterogeneous graph with compute/network nodes
- **Output:**
  - Node-level: Criticality scores (Spearman correlation)
  - Graph-level: Step time prediction (MSE + ΔT%)
- **Variants:** Bidirectional GAT vs Directed GAT

---

## 📊 Evaluation Metrics

1. **Spearman ρ:** Node criticality prediction accuracy
2. **ΔT%:** Step time prediction error percentage
3. **MSE:** Mean squared error for step time prediction
4. **Critical Fraction:** Ratio of critical nodes (target: 0.05-0.5)

---

## 🔄 Data Flow Pipeline

1. **Trace Generation:** PyTorch Profiler → Chrome traces (.json)
2. **Graph Processing:** NetworkX DAG → PyG HeteroData (.pt)
3. **Model Training:** HeteroGAT models → Multi-task learning
4. **Evaluation:** Step time prediction + Criticality scoring
5. **Optimization:** GraphRAG loop → LLM suggestions

---

## 🚀 Current Status

### ✅ **Implemented Components**
- Complete trace generation pipeline
- Graph processing and conversion
- HeteroGAT model implementation
- Multi-task training framework
- Comprehensive evaluation pipeline
- HuggingFace dataset integration

### 📋 **Planned Components** (src/ directory placeholders)
- `src/graph_pipeline/`: Production trace parsing
- `src/models/`: Model implementations
- `src/training/`: Training utilities
- `src/systems/`: Picotron integration
- `src/llm/`: GraphRAG optimization

### ❌ **Missing Components**
- Actual Python source code (notebooks contain working implementation)
- Paper LaTeX sources
- Configuration files
- Test scripts
- Documentation beyond README

---

## 🎯 Project Summary

The BottleneckOracle repository represents a comprehensive research project with a working end-to-end pipeline, primarily implemented through Jupyter notebooks, with a planned modular Python structure for future production deployment. The project successfully demonstrates the use of heterogeneous graph neural networks for predicting and explaining performance bottlenecks in LLM training jobs.

**Key Achievement:** Working pipeline from synthetic trace generation to GNN-based bottleneck prediction with multi-task learning for both step time estimation and critical node identification.

**Future Work:** Migrate notebook implementations to modular Python structure, integrate with production systems (Picotron), and develop LLM-based optimization suggestions using GraphRAG.
