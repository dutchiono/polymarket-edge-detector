# Polymarket Edge Detector v3.0

**Multi-Strategy Edge Detection System** - analyzes Polymarket markets hourly with 6 detection methods.

## 🎯 Latest Edges (Updated Hourly)

**3,142 opportunities identified** from 2,000 markets analyzed

### Edge Type Breakdown:
- **Cross-Market Arbitrage:** 3,073 edges (97.8%) - Related markets mispriced
- **Liquidity Imbalance:** 60 edges (1.9%) - Volume/Liquidity ratio signals
- **Favorite Fade:** 9 edges (0.3%) - Heavy favorites underpricing tail risk

### Top 3 Opportunities:

**1. Kraken IPO by March 31, 2026?**
- **Edge Type:** Liquidity Imbalance
- **Action:** ✅ BET YES @ $0.145
- **Fair Value:** $0.290
- **Edge:** 100.0% | **EV:** $100 per $100 bet | **Kelly:** 25.0%
- **Reasoning:** Volume/Liquidity ratio 199x - High trading activity suggests market undervaluing YES
- **Volume:** $241,645 | **Liquidity:** $1,212
- **[Trade Now →](https://polymarket.com)**

**2. [Additional top edges from sheet]**

**3. [Additional top edges from sheet]**

📊 **[View Full Edge List (Live Sheet)](https://docs.google.com/spreadsheets/d/1oFnr0HY5jQVzpZzAGwq0EVuzkSR5HJxn0bow_u_pFg8/edit#gid=559016515)**

---

## 📈 System Stats
- **Markets Analyzed:** 2,000 (sampled from 7,323 total for performance)
- **Edges Found:** 3,142 opportunities
- **Update Frequency:** Every hour
- **Last Updated:** 2026-02-11 03:00 UTC

---

## 🔍 Multi-Strategy Edge Detection (v3.0)

### **6 Detection Methods:**

**1. Pure Arbitrage**
- YES + NO prices < $0.98 (accounting for fees)
- Risk-free profit locked in
- **Tag:** PURE ARB

**2. Cross-Market Arbitrage** ⭐ Most Common
- Related markets (60%+ question similarity) with contradictory pricing
- Example: "Trump wins" priced differently across election market variants
- **Tag:** CROSS-MARKET ARB

**3. Liquidity Imbalance**
- Volume/Liquidity ratio >20x suggests price hasn't caught up to demand
- High activity signals market reassessing probabilities
- **Tag:** LIQ IMBALANCE

**4. Lottery Fade**
- Prices <$0.05 on longshot outcomes
- Behavioral bias: people overpay for exciting low-probability events
- **Tag:** LOTTERY FADE

**5. Favorite Fade**
- Prices >$0.90 on heavy favorites
- Market may underprice tail risk (black swans)
- **Tag:** FAVORITE FADE

**6. Stale Pricing**
- Low recent volume (<$1K in 24h) despite high liquidity
- Price may not reflect recent news/developments
- **Tag:** STALE PRICE

---

## 📊 Output Columns (Edge Candidates Sheet)

- **ACTION** - Clear signal: ✅ BET YES, ❌ BET NO, 👀 WATCH
- **BET SIDE** - YES or NO
- **ENTRY** - Current market price
- **FAIR** - Calculated fair value
- **EDGE %** - Percentage edge over fair value
- **EV ($)** - Expected value per $100 bet
- **KELLY %** - Recommended position size (% of bankroll)
- **LIQ SCORE** - Liquidity rating (1-10, tradability confidence)
- **PRIORITY** - HIGH/MEDIUM/LOW
- **EDGE TYPE** - Detection method used
- **MARKET QUESTION** - Full market text
- **GROUP** - Category (Sports, Politics, Crypto, Finance, Other)
- **REASONING** - Why this edge exists
- **ARB FLAG** - Additional context
- **VOLUME** - 24h trading volume
- **LIQUIDITY** - Current order book depth
- **URL** - Direct Polymarket link

**Sorted by:** Priority (PURE ARB first) then EV × Liquidity Score

---

## 🎲 How to Use This Data

### **Quick Decision Framework:**

**PURE ARB:**
- Execute immediately - risk-free profit
- No prediction needed, just math

**CROSS-MARKET ARB (97.8% of edges):**
- Research both related markets
- Confirm they're actually contradictory
- High confidence if logic is sound

**LIQ IMBALANCE + High Volume:**
- Strong signal - market is repricing
- Bet at 50-100% of Kelly depending on conviction

**LOTTERY/FAVORITE FADE:**
- Behavioral edge - requires judgment
- Smaller position sizes (25-50% Kelly)

**STALE PRICE:**
- Research recent news first
- Only bet if you confirm catalyst occurred

---

## 🛠️ Technical Implementation

**Detection Logic:**
```python
# Pure Arbitrage
if yes_price + no_price < 0.98:
    edge_type = "PURE ARB"

# Cross-Market Arbitrage  
if question_similarity > 0.60 and price_contradiction:
    edge_type = "CROSS-MARKET ARB"

# Liquidity Imbalance
if volume / liquidity > 20:
    edge_type = "LIQ IMBALANCE"
    
# Lottery Fade
if price < 0.05 and emotional_narrative:
    edge_type = "LOTTERY FADE"
    
# Favorite Fade
if price > 0.90:
    edge_type = "FAVORITE FADE"
    
# Stale Pricing
if volume_24h < 1000 and liquidity > 5000:
    edge_type = "STALE PRICE"
```

---

## 🚀 Repository Contents

- `polymarket_edge_analyzer__sheet_updater.py` - Multi-strategy edge detection
- Reads Sheet1 markets (7,323 total, 2K sample per run)
- Detects 6 edge types with reasoning
- Writes to Edge Candidates sorted by priority

---

## ⏰ Automation

**Trigger:** @trigger:hourly-polymarket-edge-detector
**Frequency:** Every hour (top of the hour)
**Platform:** Nebula workflow automation
**Updates:** Google Sheet + GitHub README automatically

---

## 📖 Version History

**v3.0 (2026-02-11 03:00 UTC):**
- Added 6 detection strategies (Pure Arb, Cross-Market, Liq Imbalance, Lottery Fade, Favorite Fade, Stale)
- Added market grouping for cross-market arbitrage detection
- Added reasoning field explaining each edge
- Changed sorting to priority-based (PURE ARB first)
- Results: 3,142 edges found (3,073 cross-market, 60 liquidity, 9 favorite)

**v2.0 (2026-02-11):**
- Added Expected Value, Kelly Criterion, Liquidity Score
- Basic arbitrage detection

**v1.0 (2026-02-10):**
- Initial edge detection

---

*Last scan: 2026-02-11 03:00 UTC | Next scan: 2026-02-11 04:00 UTC*

**Live Data:** [Google Sheet →](https://docs.google.com/spreadsheets/d/1oFnr0HY5jQVzpZzAGwq0EVuzkSR5HJxn0bow_u_pFg8/edit#gid=559016515)