---
layout: default
title: Home
---

# Polymarket Edge Detector v3.0

**Multi-Strategy Edge Detection System** - analyzes 7,300+ Polymarket markets hourly with 6 detection methods.

---

## 🎯 Latest Edges (Updated Hourly)

**3,142 opportunities identified** from 2,000 markets analyzed

### Edge Type Breakdown:
- **Cross-Market Arbitrage:** 3,073 edges (97.8%)
- **Liquidity Imbalance:** 60 edges (1.9%)
- **Favorite Fade:** 9 edges (0.3%)

---

## 🔥 Top 5 High-Conviction Edges

| Priority | Market | Action | Entry | Fair Value | Edge % | EV | Kelly % | Liq Score |
|----------|--------|--------|-------|------------|--------|-----|---------|--------|
| ⚡ HIGH | Kraken IPO by March 31, 2026? | ✅ BET YES | $0.145 | $0.290 | 100% | $100 | 25% | C (5/10) |
| ⚡ HIGH | Trump deport <250K? | ✅ BET YES | $0.038 | $0.077 | 100% | $100 | 25% | C (5/10) |
| ⚡ HIGH | Trump deport 500K-750K? | ✅ BET YES | $0.028 | $0.055 | 100% | $100 | 25% | C (5/10) |
| ⚡ HIGH | China x India clash? | ✅ BET YES | $0.135 | $0.270 | 100% | $100 | 25% | C (5/10) |
| ⚡ HIGH | DOGE cut >$250B? | ✅ BET YES | $0.011 | $0.021 | 100% | $100 | 25% | C (5/10) |

📊 **[View Full Edge List (Live Google Sheet)](https://docs.google.com/spreadsheets/d/1oFnr0HY5jQVzpZzAGwq0EVuzkSR5HJxn0bow_u_pFg8/edit#gid=559016515)**

---

## 📈 System Stats

- **Markets Analyzed:** 2,000 (sampled from 7,323 total)
- **Edges Found:** 3,142 opportunities
- **Update Frequency:** Every hour (top of the hour)
- **Last Updated:** 2026-02-11 03:00 UTC
- **Next Scan:** 2026-02-11 04:00 UTC

---

## 🔍 6 Edge Detection Strategies

### 1. 🔒 Pure Arbitrage (Risk-Free)
YES + NO prices don't sum to $1.00 after 2% fees → Lock guaranteed profit

**Priority:** CRITICAL - Execute immediately

---

### 2. ⚡ Liquidity Imbalance
Volume/Liquidity ratio >20x suggests active mispricing

**Example:** $100K volume but only $3K liquidity → High activity = undervaluation

**Priority:** HIGH (>20% edge) or MEDIUM (10-20%)

---

### 3. 🎰 Lottery Ticket Fade
Extreme longshots (<$0.05) often overpriced due to "lottery effect"

**Priority:** MEDIUM - Consider betting NO on opposite side

---

### 4. 👀 Favorite Fade
Heavy favorites (>$0.95) may underprice tail risk

**Priority:** LOW - Watch for research opportunities

---

### 5. 🔍 Stale Pricing
Low recent volume (<$1K) but high liquidity (>$5K) → Outdated prices

**Priority:** LOW - Research if recent developments occurred

---

### 6. 🔗 Cross-Market Arbitrage
Similar questions priced differently across markets

**Priority:** MEDIUM - Compare related markets for consistency

---

## 🎲 How to Use This Data

### Quick Decision Framework:

- **🔒 CRITICAL (Pure Arb):** Execute immediately - risk-free profit
- **⚡ HIGH (>20% edge):** High-conviction bet at full Kelly %
- **MEDIUM (10-20%):** Bet at 50% Kelly, do quick research
- **LOW (<10%):** Watch only, research if you have info edge

### Risk Management:
1. Never exceed Kelly % (already aggressive)
2. Reduce size for Liq Score <B
3. Diversify across edge types
4. Execute pure arbs first

---

## 🛠️ Technical Implementation

**Detection Logic:**
```python
# Pure Arbitrage
if yes_price + no_price < 0.98:
    edge_type = "PURE ARB"

# Liquidity Imbalance
if volume / liquidity > 20:
    edge_type = "LIQ IMBALANCE"
    
# Cross-Market Arbitrage  
if question_similarity > 0.60 and price_contradiction:
    edge_type = "CROSS-MARKET ARB"
```

---

## 📖 Version History

**v3.0 (2026-02-11):**
- Added 6 detection strategies
- Multi-edge reasoning system
- Priority-based sorting
- Results: 3,142 edges (3,073 cross-market, 60 liquidity, 9 favorite)

**v2.0 (2026-02-11):**
- Added EV, Kelly Criterion, Liquidity Score
- Basic arbitrage detection

**v1.0 (2026-02-10):**
- Initial edge detection

---

## 🔄 Automation

**Trigger:** Runs every hour (top of the hour)  
**Platform:** Nebula workflow automation  
**Updates:** Google Sheet + GitHub Pages automatically

---

**Repository:** [github.com/dutchiono/polymarket-edge-detector](https://github.com/dutchiono/polymarket-edge-detector)  
**Live Data:** [Google Sheet →](https://docs.google.com/spreadsheets/d/1oFnr0HY5jQVzpZzAGwq0EVuzkSR5HJxn0bow_u_pFg8/edit#gid=559016515)