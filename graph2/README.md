# Project Run Order and Outputs

## Recommended execution order

1. 02_trace_generation (1).ipynb
2. 04_v3 (1).ipynb  
   (run before nb3 so graphs_v2.pkl is ready)
3. 03_heterogat_v4.ipynb  
   (best among the 03 variants in this workspace)
4. 06_what_if_harness_final (1).ipynb

---

## What each notebook generates

### 02_trace_generation (1).ipynb

Generated files:
- traces/trace_<config>_<id>.json (raw traces)
- graphs_v2.pkl
- graph_quality_v2.png
- sample_dag_v2.png
- nb4_data_backup.zip
- traces_backup.zip

Main metrics reported:
- n_graphs (final graph count)
- avg_cp_ratio
- avg_branching_factor
- avg_slack_variance
- avg_nodes

Observed run artifact in notebook output:
- Saved 501 graphs to graphs_v2.pkl

### 04_v3 (1).ipynb

Generated files:
- graphs_v2.pkl
- graph_quality_v2.png
- sample_dag_v2.png
- nb4_data_backup.zip
- (reads traces_backup.zip and extracts to traces/)

Main metrics reported:
- n_graphs
- avg_cp_ratio
- avg_branching_factor
- avg_slack_variance
- avg_nodes
- processing summary counters: total, too_small, dag_failed, high_cp, kept

Observed run artifact in notebook output:
- Saved 501 graphs to /content/drive/MyDrive/BottleneckOracle_Backup/graphs_v2.pkl

### 03_heterogat_v4.ipynb

Generated files:
- heterogat_v2.pt (contains bidir_state, directed_state, config, test_results)
- best_Bidirectional_HeteroGAT.pt
- best_Directed_HeteroGAT_(causal_inductive_bias).pt
- checkpoint_Bidirectional_HeteroGAT.pt
- checkpoint_Directed_HeteroGAT_(causal_inductive_bias).pt

Main metrics reported:
- Spearman rho
- Delta T percent
- val_loss
- best val Spearman rho

### 06_what_if_harness_final (1).ipynb

Reads:
- heterogat_v2.pt
- graphs_v2.pkl

Generated files:
- what_if_accuracy.png

Main metrics reported:
- what-if delta_t_pct across intervention patterns
- directional agreement / intervention accuracy style checks
- harness validation checks (batch behavior, labels, model availability)

---

## 03 versions comparison (Test + Ablations)

Notes:
- Test Summary values below are from each notebook test block (Bidirectional and Directed).
- Ablation A compares Directed vs Bidirectional.
- Ablation B compares with vs without ranking loss.

| 03 Variant | Test Summary | Ablation A result | Ablation B result | Key difference between variations |
|---|---|---|---|---|
| 03_heterogat_v3 (3).ipynb | Bidir: rho=+0.511, DeltaT=5.98% ; Directed: rho=+0.219, DeltaT=10.16% | Delta rho (Directed - Bidir) = -0.292 | With ranking: +0.511 ; Without ranking: +0.516 ; Delta rho = -0.005 | Strong bidir win over directed; ranking loss did not help in this run |
| 03_heterogat_v4.ipynb | Bidir: rho=+0.548, DeltaT=11.67% ; Directed: rho=+0.509, DeltaT=10.04% | Delta rho (Directed - Bidir) = -0.040 | With ranking: +0.548 ; Without ranking: +0.589 ; Delta rho = -0.041 | Highest overall rho among v3/v4/v5 on the main test summary (chosen best variant here) |
| 03_heterogat_v5.ipynb | Bidir: rho=+0.375, DeltaT=99.72% ; Directed: rho=+0.390, DeltaT=99.13% | Delta rho (Directed - Bidir) = +0.016 | With ranking: +0.375 ; Without ranking: +0.333 ; Delta rho = +0.042 | Directed slightly better than bidir here, but DeltaT is much worse than v3/v4 |

---

## Best 03 variant in this workspace

Selected best:
- 03_heterogat_v4.ipynb

Reason:
- It has the highest top-line test Spearman among the listed 03 variants (Bidir rho=+0.548 in the test summary block).
