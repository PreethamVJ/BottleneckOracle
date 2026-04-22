# Run order

Run the notebooks in this order (top-to-bottom cells):

1. `02_v6_trace_generation.ipynb` — generates profiler trace JSONs into `./traces/`.
2. `04_v6.ipynb` — builds the graph dataset from traces and writes `graphs_v2.pkl` (plus a few PNGs).
3. `03_v6_heterogat.ipynb` — trains HeteroGAT from `graphs_v2.pkl` and saves `heterogat_v2.pt` (and checkpoints).

---

## NB04 — two real bugs to fix before running

**Bug 1:**
`augment_with_synthetic` is defined twice. The function appears in two consecutive cells (lines ~146 and ~155). The second definition is identical and will silently shadow the first — this is harmless but messy. Delete the duplicate cell.

**Bug 2:**
`load_ops_from_trace` is in the truncated section (lines 125–135 not shown) — verify it handles the Chrome trace format NB02 produces. The Chrome profiler outputs:

```
{"traceEvents": [...]}
```

with `ph`, `ts`, `dur` fields.

Make sure the loader:

* filters to `ph == "X"` (complete events)
* maps:

  * `ts → start_time`
  * `dur → duration`

If it doesn't, every trace will parse to **0 ops**, and you'll fall through entirely to synthetic data.

**Parameter check:**

* With CPU-only traces, your real graphs will mostly fail the CP filter.
* Your synthetic augmentation target is **500**.
* `generate_synthetic_graph` produces fork-join structures with exponential duration draws — these should pass:

  * `CP_THRESHOLD = 0.80`

Run the quality report cell and confirm:

* `avg_cp_ratio < 0.80`
* `avg_branching_factor > 1.30`

before proceeding to NB03.

---

## NB03 — one critical issue in the current outputs

The training logs show the model is **collapsed** — predictions are essentially constant (`-2.306...` repeated for every node across every graph).

* Spearman ρ ≈ **0.562** is real but fragile
* The model has **near-zero prediction variance**
* It’s likely sorting using a proxy feature (e.g., `topo_rank` or `out_degree`) instead of learning slack

**Evidence:**

* Target samples are also constant within each graph (`-1.6450788` repeated)
* Indicates **near-zero slack variance after z-normalization**
* Graphs are effectively **chains**, not branchy DAGs

**Root cause:**
This traces back to **NB04 data quality**.

**Fix pipeline:**

1. Fix NB04
2. Regenerate `graphs_v2.pkl` with genuinely branchy graphs
3. Retrain NB03

If ρ still doesn’t improve past ~0.65, then investigate model architecture.

---

## 2-day execution order

**Day 1:**

* Run NB04 end-to-end
* Check quality report:

  * `n_graphs ≥ 400`
  * `avg_cp_ratio < 0.80`
* Save `graphs_v2.pkl` to Drive

**Day 2:**

* Run NB03 with new dataset
* Monitor prediction variance:

  * If `pred std ≈ 0` after epoch 10 → gradient flow issue

    * Check:

      * ranking loss λ
      * Huber δ

**Target:**

* Spearman ρ > **0.65** on test set

---

## Notes

* If `./traces/` already contains the trace JSONs, you can skip step 1.
* The notebooks auto-handle Colab vs local paths via `IN_COLAB` / `DRIVE_BASE`.
* NB02 is a distraction for now — the dataset is synthetic-augmented either way.

---
