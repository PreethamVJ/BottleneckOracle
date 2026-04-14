"""
Patches 03_heterogat_fixed.ipynb:
  1. Replaces `list_repo_files, hf_hub_download` import with `snapshot_download`
  2. Replaces the graph-loading cell body to use snapshot_download from
     preethamvj/bottleneck-oracle-graphs with weights_only=False
"""
import json, re, pathlib

NB = pathlib.Path(r"d:\BottleneckOracle\notebooks\03_heterogat_fixed.ipynb")
nb = json.loads(NB.read_text(encoding="utf-8"))

for cell in nb["cells"]:
    if cell["cell_type"] != "code":
        continue
    src = cell["source"]

    # ── patch 1: imports ──────────────────────────────────────────────────────
    if "from huggingface_hub import list_repo_files, hf_hub_download" in src:
        cell["source"] = src.replace(
            "from huggingface_hub import list_repo_files, hf_hub_download",
            "from huggingface_hub import snapshot_download"
        )
        print("✅ Patched: imports")

    # ── patch 2: loading cell ─────────────────────────────────────────────────
    if 'REPO = "archi829/bottleneck-oracle-graphs"' in src or \
       "archi829/bottleneck-oracle-graphs" in src:

        cell["source"] = '''\
REPO = "preethamvj/bottleneck-oracle-graphs"

# Download entire dataset snapshot (faster than per-file downloads)
path = snapshot_download(repo_id=REPO, repo_type="dataset")
print(f"Snapshot downloaded to: {path}")

graphs = []
for f in sorted(os.listdir(path)):
    if f.endswith(".pt"):
        g = torch.load(f"{path}/{f}", weights_only=False)
        graphs.append(g)

print(f"Loaded {len(graphs)} graphs")

# ── quick sanity on one graph ─────────────────────────────────────────────────
g0 = graphs[0]
assert g0['compute'].x.shape[1] == 4, "Expected 4 compute features"
assert g0['compute'].y is not None,    "Missing node labels"
assert g0.y is not None,               "Missing graph label"
print(f"Graph schema: {g0}")
print(f"Compute nodes: {g0['compute'].x.shape[0]}")
print(f"Edge types: {g0.edge_types}")
'''
        print("✅ Patched: graph-loading cell")

NB.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
print("✅ Notebook saved.")
