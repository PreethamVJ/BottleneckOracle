import pandas as pd
from datetime import datetime

# Project plan data with truthful status assessment
project_data = [
    # Epic 1, Sprint 1
    ["Epic 1: Trace ingestion & 2-tier DAG construction", "Sprint 1: Picotron instrumentation",
     "Profiler transformer model using Pytorch Profiler, hook timing events",
     "PyTorch Profiler records all ops with timings; chrome trace exported successfully",
     "✅ DONE", "01_trace_generation_ipynb.ipynb, 02-trace-generation-fixed.ipynb"],

    ["Epic 1: Trace ingestion & 2-tier DAG construction", "Sprint 1: Picotron instrumentation",
     "Run config sweeps, validate critical-path rank vs analytic ground truth",
     "3 different model sizes/configs (tiny, small, medium)",
     "✅ DONE", "02-trace-generation-fixed.ipynb - 3 configs implemented"],

    ["Epic 1: Trace ingestion & 2-tier DAG construction", "Sprint 1: Picotron instrumentation",
     "Build Chakra → NetworkX parser: nodes typed, edges correctly directed",
     "All nodes typed (software + network tiers), edges directed, no bidirectional leakage",
     "✅ DONE", "02-trace-generation-fixed.ipynb - NetworkX DAG construction"],

    ["Epic 1: Trace ingestion & 2-tier DAG construction", "Sprint 1: Picotron instrumentation",
     "NetworkX → PyG HeteroData conversion",
     "HeteroData loads cleanly into PYG; node/edge feature shapes verified",
     "✅ DONE", "03_heterogat_fixed.ipynb - PyG conversion implemented"],

    ["Epic 1: Trace ingestion & 2-tier DAG construction", "Sprint 1: Picotron instrumentation",
     "Derive HW proxy features from trace stats",
     "Per-node proxy features (compute ratio, comm/compute ratio) non-zero and normalized",
     "✅ DONE", "02-trace-generation-fixed.ipynb - features computed"],

    # Epic 1, Sprint 2
    ["Epic 1: Trace ingestion & 2-tier DAG construction", "Sprint 2: Baseline analytical model",
     "1F1B analytic formula baseline implemented",
     "MSE + ΔT error table ready on held-out graphs",
     "✅ DONE", "model_1f1b.ipynb - 1F1B baseline implemented"],

    ["Epic 1: Trace ingestion & 2-tier DAG construction", "Sprint 2: Baseline analytical model",
     "MLP skeleton on flattened features ready; train/val/test splits defined",
     "MLP trains without error; splits fixed and shared with team",
     "✅ DONE", "model_1f1b.ipynb - MLP baseline + splits"],

    # Epic 2, Sprint 3
    ["Epic 2: Baseline models", "Sprint 3: Non-graph baselines",
     "MLP + XGBoost baselines, hyperparameter sweep done",
     "Table 1 numbers logged — MSE + ΔT accuracy for both models across 3 seeds",
     "🟡 PARTIAL", "model_1f1b.ipynb - MLP done, XGBoost + hyperparameter sweep needed"],

    ["Epic 2: Baseline models", "Sprint 3: Non-graph baselines",
     "Compile Table 1: 1F1B vs MLP vs XGBoost",
     "Table populated, consistent across 3 seeds, ready for GNN comparison",
     "🟡 PARTIAL", "Needs XGBoost completion for full Table 1"],

    # Epic 3, Sprint 4
    ["Epic 3: HeteroGAT + Directed message passing", "Sprint 4: HeteroGAT both variants",
     "Variant A: standard bidirectional HeteroGAT (associational baseline)",
     "2-layer HeteroGAT trains, loss curves stable, slack predictions visible, attn weights extractable",
     "✅ DONE", "03_heterogat_fixed.ipynb - bidirectional HeteroGAT implemented"],

    ["Epic 3: HeteroGAT + Directed message passing", "Sprint 4: HeteroGAT both variants",
     "Variant B: directed topological message passing (causal inductive bias)",
     "Messages flow ancestor→descendant only, respects DAG topology, plugs into same training loop",
     "✅ DONE", "03_heterogat_fixed.ipynb - directed variant implemented"],

    ["Epic 3: HeteroGAT + Directed message passing", "Sprint 4: HeteroGAT both variants",
     "Multi-task heads: predict step time + per-node slack jointly",
     "Both task heads show decreasing val loss across both variants",
     "✅ DONE", "03_heterogat_fixed.ipynb - multi-task learning implemented"],

    ["Epic 3: HeteroGAT + Directed message passing", "Sprint 4: HeteroGAT both variants",
     "Build perturbation what-if harness: edit node → GNN forward pass → predict ΔT",
     "Given trained GNN + edited graph, returns predicted ΔT. Interface contract agreed by W3 end.",
     "❌ NOT DONE", "Needs dedicated notebook - intervention harness not implemented"],

    # Epic 3, Sprint 5
    ["Epic 3: HeteroGAT + Directed message passing", "Sprint 5: Ablations + interventional eval",
     "Ablation A: directed vs bidirectional — Spearman ρ vs analytic critical path",
     "ρ > 0.7 for directed variant; ΔT error < 5%",
     "🟡 PARTIAL", "Models trained, but systematic ablation study needed"],

    ["Epic 3: HeteroGAT + Directed message passing", "Sprint 5: Ablations + interventional eval",
     "Ablation B: HW proxy tier removed vs full graph — MAE delta",
     "MAE delta documented — positive or negative result both acceptable",
     "❌ NOT DONE", "Ablation study not conducted"],

    ["Epic 3: HeteroGAT + Directed message passing", "Sprint 5: Ablations + interventional eval",
     "Run ΔT what-if eval: compare GNN prediction vs simulator rerun",
     "GNN-predicted ΔT within acceptable error of STAGE re-simulation on ≥10 edited graphs",
     "❌ NOT DONE", "Requires what-if harness completion first"],

    ["Epic 3: HeteroGAT + Directed message passing", "Sprint 5: Ablations + interventional eval",
     "OOD splits: train depth 2–4, test depth 6–8 — MAE degradation table",
     "OOD MAE reported; degradation documented as limitation if > 20%",
     "❌ NOT DONE", "No OOD generalization experiments conducted"],

    # Epic 4, Sprint 6
    ["Epic 4: GraphRAG optimizer loop (LLM Role 3)", "Sprint 6: GraphRAG loop",
     "Serialize causal subgraph → structured LLM prompt with node IDs + slack scores",
     "Prompt template finalized, fits context window, node IDs traceable back to graph",
     "❌ NOT DONE", "GraphRAG components not started"],

    ["Epic 4: GraphRAG optimizer loop (LLM Role 3)", "Sprint 6: GraphRAG loop",
     "Generate NL optimizer suggestions for ≥20 graphs via LLM API",
     "Ranked suggestions (microbatch tuning, stage remapping) returned for each graph",
     "❌ NOT DONE", "LLM integration not started"],

    ["Epic 4: GraphRAG optimizer loop (LLM Role 3)", "Sprint 6: GraphRAG loop",
     "Validate top-3 suggestions: re-run GNN forward pass on counterfactually edited graph",
     "≥2 of 3 top suggestions reduce predicted ΔT when applied — suggestion accuracy metric logged",
     "❌ NOT DONE", "Depends on GraphRAG completion"],

    ["Epic 4: GraphRAG optimizer loop (LLM Role 3)", "Sprint 6: GraphRAG loop",
     "Recall@1 automated eval: does top suggestion match known bottleneck?",
     "Recall@1 computed across ≥20 graphs, results table ready for paper",
     "❌ NOT DONE", "Depends on GraphRAG completion"],
]

# Create DataFrame
df = pd.DataFrame(project_data, columns=[
    "Epic", "Sprint", "Story", "Acceptance Criterion", "Status", "Notes/Location"
])

# Add summary statistics
summary_stats = {
    "Total Stories": len(project_data),
    "Completed": sum(1 for x in project_data if x[4] == "✅ DONE"),
    "Partial": sum(1 for x in project_data if x[4] == "🟡 PARTIAL"),
    "Not Done": sum(1 for x in project_data if x[4] == "❌ NOT DONE"),
    "Completion %": f"{sum(1 for x in project_data if x[4] == '✅ DONE') / len(project_data) * 100:.1f}%"
}

# Create Excel writer with multiple sheets
with pd.ExcelWriter('PROJECT_STATUS_TRACKER.xlsx', engine='openpyxl') as writer:
    # Main tracking sheet
    df.to_excel(writer, sheet_name='Project Status', index=False)

    # Summary sheet
    summary_df = pd.DataFrame(list(summary_stats.items()), columns=['Metric', 'Value'])
    summary_df.to_excel(writer, sheet_name='Summary', index=False)

    # Epic breakdown sheet
    epic_breakdown = df.groupby('Epic').agg({
        'Status': lambda x: f"{sum(x == '✅ DONE')}/{len(x)} completed"
    }).reset_index()
    epic_breakdown.to_excel(writer, sheet_name='Epic Breakdown', index=False)

    # Sprint breakdown sheet
    sprint_breakdown = df.groupby('Sprint').agg({
        'Status': lambda x: f"{sum(x == '✅ DONE')}/{len(x)} completed"
    }).reset_index()
    sprint_breakdown.to_excel(writer, sheet_name='Sprint Breakdown', index=False)

print(f"PROJECT_STATUS_TRACKER.xlsx created successfully!")
print(f"\nSummary Statistics:")
for metric, value in summary_stats.items():
    print(f"   {metric}: {value}")
