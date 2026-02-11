---
layout: default
title: Home
---

# Polymarket Edge Detector v3.0

**Multi-Strategy Edge Detection System** - analyzes 7,300+ Polymarket markets hourly with 6 detection methods.

---

## 🎯 Latest Edges (Updated Hourly)

**887 opportunities identified** from 1,239 active markets analyzed

### Edge Type Breakdown:
- **Lottery Fade:** 755 edges (85.1%)
- **Liquidity Imbalance:** 103 edges (11.6%)
- **Favorite Fade:** 29 edges (3.3%)
- **Pure Arbitrage:** 0 edges (0.0%)

---

## 🔥 Top 5 High-Conviction Edges

| Priority | Market | Action | Entry | Edge Type |
|----------|--------|--------|-------|-----------|
| ⚡ HIGH | Trump deport 250K-500K? | ✅ BET YES | $0.904 | 505x liq imbalance |
| ⚡ HIGH | Harvey Weinstein 10-20yr? | ❌ BET NO | $0.895 | 477x liq imbalance |
| ⚡ HIGH | SCOTUS sports contract case? | ✅ BET YES | $0.335 | 276x liq imbalance |
| ⚡ HIGH | Kraken IPO by March 31? | ✅ BET YES | $0.145 | 199x liq imbalance |
| ⚡ HIGH | Caroline van der Plas PM? | ❌ BET NO | $1.000 | 194x liq imbalance |

📊 **[View Full Edge List (Live Google Sheet)](https://docs.google.com/spreadsheets/d/1oFnr0HY5jQVzpZzAGwq0EVuzkSR5HJxn0bow_u_pFg8/edit#gid=559016515)**

---

## 📈 System Stats

- **Total Markets:** 7,323 markets in Polymarket
- **Markets Analyzed:** 1,239 active markets
- **Edges Found:** 887 opportunities
- **Update Frequency:** Every hour (top of the hour)
- **Last Updated:** 2026-02-11 04:00 UTC
- **Next Scan:** 2026-02-11 05:00 UTC

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

### 5. 📉 Stale Pricing
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

### Liquidity Scores:
- **A (9-10):** Excellent - Trade full size
- **B (7-8):** Good - Trade 75% size
- **C (5-6):** Fair - Trade 50% size
- **D (3-4):** Poor - Trade 25% or skip
- **F (1-2):** Very Poor - Avoid

---

## 📊 Understanding the Data

### Key Metrics:
- **Edge %:** How much better than fair value (higher = better)
- **EV ($):** Expected profit per $100 bet
- **Kelly %:** Recommended position size (% of bankroll)
- **Liq Score:** Can you actually trade this? (1-10 scale)

### Edge Types Explained:
- **LIQ IMBALANCE:** High volume/liquidity ratio → Market catching up to new info
- **LOTTERY FADE:** Extreme longshots overpriced → Bet against them
- **FAVORITE FADE:** Heavy favorites underpricing tail risk → Small NO bet
- **PURE ARB:** YES + NO < $1.00 → Free money (rare)
- **CROSS-MARKET ARB:** Same event priced differently → Exploit gap
- **STALE PRICE:** Low recent volume → May not reflect news

---

## 🔗 Resources

- **[Live Google Sheet - Full Edge List](https://docs.google.com/spreadsheets/d/1oFnr0HY5jQVzpZzAGwq0EVuzkSR5HJxn0bow_u_pFg8/edit#gid=559016515)**
- **[GitHub Repository](https://github.com/dutchiono/polymarket-edge-detector)**
- **[Polymarket Platform](https://polymarket.com)**

---

## 📝 Methodology

- **Data Source:** Polymarket Gamma API
- **Update Schedule:** Every hour at :00
- **Sampling:** 1,239 active markets (from 7,323 total)
- **Fair Value:** Cross-market analysis + liquidity flows
- **Kelly Sizing:** Conservative (25% max) for model uncertainty
- **Liquidity Scoring:** Depth + spread + volume analysis

---

## ⚠️ Disclaimer

Educational/informational purposes only. Not financial advice. Markets can remain irrational longer than you can remain solvent. Always do your own research. Past performance does not guarantee future results.

---

**Built with:** Python • Google Sheets API • Polymarket Gamma API • Nebula AI  
**Version:** 3.0 (Multi-Strategy Detection)  
**Status:** Live (Hourly Updates)
