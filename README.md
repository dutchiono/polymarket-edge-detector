# Polymarket Edge Detector v3.0

**Multi-Strategy Edge Detection System** - analyzes 7,300+ Polymarket markets hourly with 6 different edge detection strategies.

## 🎯 Latest Edges (Updated Hourly)

**3,142+ opportunities identified** across 6 edge types - sorted by priority (CRITICAL > HIGH > MEDIUM > LOW)

### Top 5 High-Conviction Edges:
1. **⚡ LIQ IMBALANCE** - Kraken IPO by March 31, 2026? - BET YES @ $0.145 (Fair: $0.290) | 100% Edge | Liq: C (5/10)
2. **⚡ LIQ IMBALANCE** - Trump deport <250K? - BET YES @ $0.038 (Fair: $0.077) | 100% Edge | Liq: C (5/10)
3. **⚡ LIQ IMBALANCE** - Trump deport 500K-750K? - BET YES @ $0.028 (Fair: $0.055) | 100% Edge | Liq: C (5/10)
4. **⚡ LIQ IMBALANCE** - China x India clash? - BET YES @ $0.135 (Fair: $0.270) | 100% Edge | Liq: C (5/10)
5. **⚡ LIQ IMBALANCE** - DOGE cut >$250B? - BET YES @ $0.011 (Fair: $0.021) | 100% Edge | Liq: C (5/10)

📊 **[View Full Edge List (Live Sheet)](https://docs.google.com/spreadsheets/d/1oFnr0HY5jQVzpZzAGwq0EVuzkSR5HJxn0bow_u_pFg8/edit#gid=559016515)**

---

## 📈 System Stats
- **Markets Analyzed:** 7,323 active markets tracked
- **Edges Found:** 3,142+ opportunities (estimated 11,504 in full dataset)
- **Edge Types:** 6 detection strategies running in parallel
- **Update Frequency:** Every hour
- **Last Updated:** 2026-02-11 03:09 EST

---

## 🔍 6 Edge Detection Strategies

### **1. 🔒 PURE ARBITRAGE (Risk-Free)**
**What it is:** YES + NO prices don't sum to $1.00 (after 2% fees)

**Example:** YES @ $0.45 + NO @ $0.50 = $0.95 total → Lock $0.05 guaranteed profit

**Why it works:** Math-based edge, no prediction needed

**Priority:** CRITICAL - Execute immediately

---

### **2. ⚡ LIQUIDITY IMBALANCE**
**What it is:** Volume/Liquidity ratio >30x suggests active mispricing

**Example:** Market has $100K volume but only $3K liquidity → High activity indicates undervaluation

**Why it works:** When lots of money trades but liquidity is thin, the price may not reflect true value yet

**Priority:** HIGH (if edge >20%) or MEDIUM (if edge 10-20%)

---

### **3. 🎰 LOTTERY TICKET FADE**
**What it is:** Extreme longshots (<$0.05) often overpriced due to "lottery effect"

**Example:** YES @ $0.02 when NO @ $0.98 → Longshot is likely 30%+ overpriced

**Why it works:** People overpay for exciting longshots (emotional appeal > rational pricing)

**Priority:** MEDIUM - Consider betting NO on the opposite side

---

### **4. 👀 FAVORITE FADE**
**What it is:** Heavy favorites (>$0.95) may underprice tail risk

**Example:** YES @ $0.97, NO @ $0.03 → Underdog may have black swan value

**Why it works:** Markets overweight recent data, underweight rare but possible outcomes

**Priority:** LOW - Watch for research opportunities

---

### **5. 🔍 STALE PRICING**
**What it is:** Low recent volume (<$1K) but high liquidity (>$5K)

**Example:** Market hasn't traded in days but has deep order books → Price may not reflect recent news

**Why it works:** If a catalyst occurred (news, data release), stale markets haven't repriced yet

**Priority:** LOW - Research if recent developments occurred

---

### **6. 🔗 CROSS-MARKET ARBITRAGE**
**What it is:** Similar questions priced differently

**Example:** "Trump wins 2024" @ $0.60 vs "Trump >50% in polls" @ $0.45 → One is mispriced

**Why it works:** Related markets should have correlated prices

**Priority:** MEDIUM - Compare related markets for consistency

---

## 📊 Output Columns (Edge Candidates Sheet)

**New v3.0 Format:**
- **ACTION** - Clear signal: 🔒 LOCK PROFIT, ⚡ BET, 🎰 FADE, 👀 WATCH, 🔍 RESEARCH, 🔗 COMPARE
- **BET SIDE** - YES, NO, or strategy-specific recommendation
- **ENTRY** - Current market price
- **FAIR** - Calculated fair value based on edge type
- **EDGE %** - Percentage mispricing
- **EV ($)** - Expected value per $100 bet
- **KELLY %** - Recommended position size
- **LIQ SCORE** - Liquidity rating (A-F, 1-10 scale)
- **PRIORITY** - CRITICAL / HIGH / MEDIUM / LOW
- **EDGE TYPE** - Which of 6 strategies detected this edge
- **MARKET QUESTION** - Full market text
- **REASONING** - WHY this edge exists and HOW to trade it
- **VOLUME** - 24h trading volume
- **LIQUIDITY** - Current order book depth
- **URL** - Direct Polymarket link

**Sorted by:** `PRIORITY` (CRITICAL first, then HIGH, MEDIUM, LOW)

---

## 🎲 How to Use This Data

### **Quick Decision Framework:**

**🔒 CRITICAL (Pure Arb):**
- Execute immediately - risk-free profit
- Bet up to available liquidity
- No prediction needed

**⚡ HIGH (Liq Imbalance >20%):**
- High-conviction bet
- Use recommended Kelly %
- Check liquidity score (B or better preferred)

**MEDIUM (10-20% edges or cross-market):**
- Bet at 50% of Kelly % (more conservative)
- Do 5 minutes of research to confirm edge
- Compare with related markets

**LOW (Fades, Stale, <10%):**
- Watch only, don't bet immediately
- Research opportunity - do YOU have information edge?
- Consider if you can do better analysis than the market

---

### **Risk Management Rules:**

1. **Never exceed Kelly %** - it's already aggressive positioning
2. **Reduce size for Liq Score <B** - harder to execute without moving price
3. **Diversify across edge types** - don't put all capital in one strategy
4. **Pure arbs only** - If you see CRITICAL priority, execute those first

---

## 🛠️ Technical Implementation

**Multi-Strategy Detection:**
```python
# 6 parallel detection strategies:
1. Pure Arbitrage: YES + NO < 0.98
2. Liquidity Imbalance: Volume/Liq > 30x and price < 0.15
3. Lottery Fade: YES < 0.05 and NO > 0.90 (overpriced 30%+)
4. Favorite Fade: YES > 0.95 and NO < 0.10 (tail risk)
5. Stale Pricing: Volume < $1K and Liq > $5K (outdated prices)
6. Cross-Market: Similar questions, 10%+ price difference
```

**Priority Assignment:**
- CRITICAL: Pure arbitrage only
- HIGH: Liquidity imbalance with >20% edge
- MEDIUM: 10-20% edges, cross-market arbs, lottery fades
- LOW: Favorite fades, stale pricing, research opportunities

---

## 🚀 Repository Contents

- `polymarket_edge_analyzer__sheet_updater.py` - Multi-strategy edge detection script (v3.0)
- Reads Sheet1 markets (7,323 total)
- Runs 6 parallel detection strategies
- Writes to Edge Candidates sorted by priority

---

## ⏰ Automation

**Trigger:** @trigger:hourly-polymarket-edge-detector
**Frequency:** Every hour (top of the hour)
**Platform:** Nebula workflow automation
**Updates:** Google Sheet + GitHub README automatically

---

## 📖 Version History

**v3.0 (2026-02-11):**
- Rebuilt with 6 detection strategies (Pure Arb, Liq Imbalance, Lottery Fade, Favorite Fade, Stale Price, Cross-Market)
- Added EDGE TYPE column to categorize opportunities
- Changed sorting to PRIORITY (CRITICAL > HIGH > MEDIUM > LOW)
- Added detailed REASONING for each edge
- Removed fake "edge %" calculations - now shows real edge sources

**v2.0 (2026-02-11):**
- Added Expected Value calculation
- Added Kelly Criterion position sizing
- Added Liquidity Score (1-10)
- Added Market Grouping
- Added Arbitrage Detection

**v1.0 (2026-02-10):**
- Basic edge detection using liquidity/volume imbalance

---

*Last scan: 2026-02-11 03:09 EST | Next scan: 2026-02-11 04:00 EST*