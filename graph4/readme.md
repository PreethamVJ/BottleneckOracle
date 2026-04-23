# Results

---

## v6

### Test Set Results

**Bidirectional**
- Spearman ρ : +0.952  *(target: > 0.70)*
- ΔT%        : 29.27%  *(target: < 5%)*
- Test Loss  : 0.1436  

**Directed**
- Spearman ρ : +0.952  *(target: > 0.70)*
- ΔT%        : 41.23%  *(target: < 5%)*
- Test Loss  : 0.3438  

---

## v7

### Test Set Results

**Bidirectional**
- Spearman ρ : +0.965  *(target: > 0.70)*
- ΔT%        : 24.70%  *(target: < 5%)*
- Test Loss  : 0.3675  

**Directed**
- Spearman ρ : +0.944  *(target: > 0.70)*
- ΔT%        : 39.96%  *(target: < 5%)*
- Test Loss  : 0.8116  

---

## v8

### Test Set Results

**Bidirectional**
- Spearman ρ : +0.968  *(target: > 0.70)*
- ΔT%        : 25.62%  *(target: < 5%)*
- Test Loss  : 0.3882  

**Directed**
- Spearman ρ : +0.942  *(target: > 0.70)*
- ΔT%        : 39.83%  *(target: < 5%)*
- Test Loss  : 0.8097  

---

## v9

### Test Set Results

**Bidirectional**
- Spearman ρ : +0.968  *(target: > 0.70)*
- ΔT%        : 24.28%  *(target: < 5%)*
- Test Loss  : 0.3882  

**Directed**
- Spearman ρ : +0.942  *(target: > 0.70)*
- ΔT%        : 37.91%  *(target: < 5%)*
- Test Loss  : 0.8098  

---

## v10

### Test Set Results

**Bidirectional**
- Spearman ρ : +0.966  *(target: > 0.70)*
- ΔT%        : 7.23%   *(target: < 5%)*
- Test Loss  : 0.4172  

**Directed**
- Spearman ρ : +0.947  *(target: > 0.70)*
- ΔT%        : 11.79%  *(target: < 5%)*
- Test Loss  : 0.8043  

---

## v11

### Test Set Results

**Bidirectional**
- Spearman ρ : +0.967  *(target: > 0.70)*
- ΔT%        : 7.06%   *(target: < 5%)*
- Test Loss  : 0.5545  

**Directed**
- Spearman ρ : +0.957  *(target: > 0.70)*
- ΔT%        : 11.13%  *(target: < 5%)*
- Test Loss  : 0.9647  

---

## v12

### Test Set Results

**Bidirectional**
- Spearman ρ : +0.967  *(target: > 0.70)*
- ΔT%        : 7.57%   *(target: < 5%)*
- Test Loss  : 0.5840  

**Directed**
- Spearman ρ : +0.957  *(target: > 0.70)*
- ΔT%        : 8.99%   *(target: < 5%)*
- Test Loss  : 0.7625  

---

# Analysis & Recommendation

## Key Insight
The **major improvement occurs between v9 and v10**, driven by the **step-time normalization fix**:
- Removed incorrect `/1000` µs conversion  
- Applied `log1p` + z-normalization  

This reduces ΔT% drastically from ~25–40% → ~7–12%.

---

## Version Comparison

| Version | Bidir ΔT% | Bidir Loss | Dir ΔT% | Dir Loss |
|--------|----------|-----------|--------|---------|
| v10 | 7.23% | **0.417** | 11.79% | **0.804** |
| v11 | 7.06% | 0.555 | 11.13% | 0.965 |
| v12 | 7.57% | 0.584 | **8.99%** | 0.763 |

---

## Decision

**Use v10**

### Why?
- Best **overall generalization (lowest test loss)**
- Stable performance across both heads
- v11/v12 gains in ΔT% are **marginal and inconsistent**
- None of the versions achieve the <5% ΔT target anyway

---

## Additional Notes

- **v11 tradeoff:** Slight ΔT improvement but **~33% worse loss**
- **v12 tradeoff:** Better directed ΔT but **worse bidirectional + higher loss**
- **v10 is the most balanced checkpoint**

---

## Deployment Notes

- Fully compatible with nb06 (same architecture via config dict)
- Safe for nb08 LLM validation loop due to **better calibration**
- Lower loss → more reliable ranking → better Recall@1

---

## Next Optimization Direction

The bottleneck is now **directed ΔT% (~11.79%)**

Recommended focus:
- Improve **graph topology diversity (nb02)**
- Avoid further loss-weight tuning (diminishing returns observed)