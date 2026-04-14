# BottleneckOracle - Notebook-First Implementation

## 📁 Repository Structure

```
BottleneckOracle/
├── PROJECT_STATUS_TRACKER.xlsx    # Truthful project progress tracking
├── REPOSITORY_STRUCTURE.md        # Complete repository documentation
├── README.md                      # Original project documentation
├── requirements.txt               # Python dependencies
├── legacy/                        # Superseded code & utility scripts
└── notebooks/                     # Working code + completion plan
    ├── 01_working_baselines.ipynb         # ✅ 1F1B + MLP baselines (DONE)
    ├── 02_data_generation.ipynb           # ✅ Trace generation pipeline (DONE)
    ├── 03_heterogat_models.ipynb          # ✅ HeteroGAT variants (DONE)
    ├── 04_dag_construction.ipynb          # ✅ Timing-based DAG construction (DONE)
    ├── 05_xgboost_baseline_completion.ipynb # 🟡 Complete XGBoost + Table 1 (TODO)
    ├── 06_what_if_harness.ipynb           # ❌ Intervention harness (TODO)
    ├── 07_ablation_studies.ipynb          # ❌ Ablation studies (TODO)
    └── 08_graphrag_optimizer.ipynb        # ❌ LLM integration (TODO)
```

## 🎯 Current Project Status (47.6% Complete)

### ✅ **Completed (10/21 stories)**
- **Epic 1**: Trace ingestion & DAG construction ✅
  - PyTorch Profiler integration ✅
  - NetworkX DAG construction ✅
  - PyG HeteroData conversion ✅
  - Hardware proxy features ✅
  - 1F1B baseline ✅
  - MLP baseline ✅

- **Epic 3**: HeteroGAT variants ✅
  - Bidirectional HeteroGAT ✅
  - Directed message passing ✅
  - Multi-task learning ✅

### 🟡 **Partial (3/21 stories)**
- **Epic 2**: Non-graph baselines
  - MLP completed, XGBoost + hyperparameter sweep needed

### ❌ **Not Done (8/21 stories)**
- **Epic 3**: Ablation studies (Sprint 5)
- **Epic 4**: GraphRAG optimizer loop (Sprint 6)

## 📓 Notebook Structure

### **✅ Working Notebooks (DONE)**
**Notebook 01: Working Baselines** (`01_working_baselines.ipynb`)
- **Status**: ✅ COMPLETE
- **Contains**: 1F1B analytic formula + MLP baseline
- **Results**: MSE + ΔT error metrics, train/val/test splits
- **Usage**: Reference for baseline comparisons, load trained MLP models

**Notebook 02: Data Generation** (`02-trace-generation-fixed.ipynb`) 
- **Status**: ✅ COMPLETE - **TEAMMATE'S WORK - UNCHANGED**
- **Contains**: Complete trace generation pipeline with HuggingFace integration
- **Features**: Fixed graph edge construction, multi-task heads, 501 synthetic graphs
- **Usage**: Load this dataset for all subsequent experiments

**Notebook 03: HeteroGAT Models** (`03_heterogat_fixed.ipynb`)
- **Status**: ✅ COMPLETE - **TEAMMATE'S WORK - UNCHANGED**
- **Contains**: Both bidirectional + directed HeteroGAT variants
- **Features**: 2-layer heterogeneous GNN, multi-task learning, comprehensive evaluation
- **Usage**: Load trained models for what-if analysis and ablations

**Notebook 04: DAG Construction** (`04_timing_based_dag.ipynb`)
- **Status**: ✅ COMPLETE - **TEAMMATE'S WORK - UNCHANGED**
- **Contains**: Timing-based DAG construction with genuine parallelism
- **Features**: Realistic edge creation, critical path labeling
- **Usage**: Reference for graph construction methodology

### **🟡 Completion Notebooks (TODO)**
**Notebook 05: XGBoost Completion** (`05_xgboost_baseline_completion.ipynb`)
- **Status**: 🟡 PARTIAL (MLP done, XGBoost needed)
- **Purpose**: Complete Epic 2 non-graph baselines
- **Tasks**: Implement XGBoost + hyperparameter sweep, finish Table 1

**Notebook 06: What-If Harness** (`06_what_if_harness.ipynb`)
- **Status**: ❌ NOT DONE
- **Purpose**: Build intervention harness for Epic 3, Sprint 4
- **Tasks**: Graph editing interface, ΔT prediction engine, intervention patterns

**Notebook 07: Ablation Studies** (`07_ablation_studies.ipynb`)
- **Status**: ❌ NOT DONE
- **Purpose**: Complete Epic 3 evaluation and W5 checkpoint
- **Tasks**: Directed vs bidirectional comparison, HW proxy removal, what-if validation, OOD tests

**Notebook 08: GraphRAG Optimizer** (`08_graphrag_optimizer.ipynb`)
- **Status**: ❌ NOT DONE
- **Purpose**: Implement Epic 4 LLM integration (pending W5 gate)
- **Tasks**: Graph serialization, LLM suggestions, validation, Recall@1 evaluation

## 🚀 Execution Path

1. **Start with Notebook 01**: Review working baselines (1F1B + MLP)
2. **Use Notebook 02**: Understand data generation pipeline and load dataset
3. **Load from Notebook 03**: Get trained HeteroGAT models for experiments
4. **Complete Notebook 05**: Add XGBoost baseline to finish Table 1
5. **Build Notebook 06**: Create what-if harness (needed for ablations)
6. **Run Notebook 07**: Execute ablation studies and W5 checkpoint gate
7. **Maybe Notebook 08**: LLM integration (only if W5 gate passes)

## 📂 Legacy Folder Contents

The `legacy/` folder contains superseded or utility files:
- `01_trace_generation_ipynb.ipynb` - Old proof-of-concept (superseded by Notebook 02)
- `Citation.ris` - Placeholder citation file
- `patch_nb03.py` - Utility script for notebook compatibility
- `create_status_tracker.py` - Script that generated PROJECT_STATUS_TRACKER.xlsx
- `src/`, `paper/` - Empty directory structures for future modularization

## 📊 Key Metrics to Track

- **Sprint 3**: Table 1 completion (1F1B vs MLP vs XGBoost)
- **Sprint 4**: What-if harness interface contract
- **Sprint 5**: 
  - Spearman ρ > 0.7 for directed variant
  - ΔT error < 5%
  - OOD degradation < 20%
- **Sprint 6**: Recall@1 and suggestion accuracy

## 🔗 Dependencies & Workflow

**IMPORTANT: Teammate's Preserved Work**
- `02-trace-generation-fixed.ipynb` → **Your teammate's work - UNCHANGED**
- `03_heterogat_fixed.ipynb` → **Your teammate's work - UNCHANGED** 
- `04_timing_based_dag.ipynb` → **Your teammate's work - UNCHANGED**
- **Only moved from legacy/ - no code modifications, ownership preserved**

**Data Flow:**
- `02-trace-generation-fixed.ipynb` → generates dataset stored on HuggingFace
- `01_working_baselines.ipynb` → trained baselines (1F1B + MLP)
- `03_heterogat_fixed.ipynb` → trained HeteroGAT models
- `04_timing_based_dag.ipynb` → DAG construction methodology

**Completion Chain:**
- Notebook 01 results → Notebook 05 (finish Table 1)
- Notebook 03 models → Notebook 06 (what-if harness)
- Notebook 06 harness → Notebook 07 (ablation studies)
- Notebook 07 results → Decision: Notebook 08 or more ablations

**External Resources:**
- HuggingFace Dataset: `preethamvj/bottleneck-oracle-graphs`
- PROJECT_STATUS_TRACKER.xlsx: Detailed project status

## 💡 Key Insights

**Working Code (Notebooks 01-04):**
- ✅ Complete end-to-end pipeline implemented
- ✅ Trained models ready for use
- ✅ Proven methodology with 501 synthetic graphs

**Completion Focus (Notebooks 05-08):**
- 🟡 Notebook 05: Add XGBoost to existing baselines
- ❌ Notebooks 06-08: Structure ready, implementation needed
- 🎯 Clear path from 47.6% to 100% completion

## 📊 Project Truth

**What Actually Works:**
- Trace generation: PyTorch Profiler → NetworkX → PyG HeteroData ✅
- Baselines: 1F1B analytic + MLP with proper splits ✅
- GNN Models: Both HeteroGAT variants trained and evaluated ✅
- Data: 501 graphs across 3 model configs ✅

**What Needs Completion:**
- Baselines: XGBoost + hyperparameter sweep 🟡
- Interventions: What-if prediction system ❌
- Analysis: Ablation studies and OOD tests ❌
- LLM: GraphRAG optimization loop ❌

---

**Last Updated**: 2026-04-14  
**Completion**: 47.6% (10/21 stories completed)  
**Strategy**: Build on working foundations (Notebooks 01-04) to complete remaining work systematically