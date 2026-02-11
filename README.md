# Polymarket Edge Detector v2.0

**Advanced automated edge detection system** - analyzes 7,300+ Polymarket markets hourly with multi-dimensional risk metrics.

## 🎯 Latest Edges (Updated Hourly)

**117 opportunities identified** - sorted by Expected Value × Liquidity Score (actual tradeable profit)

### Top 5 Edges Right Now:
1. **✅ BET YES @ $0.099** - GDP growth >2.5% - 14.8% edge, $150 EV, 7.4% Kelly, Liq: 4/10
2. **✅ BET YES @ $0.096** - Marty Supreme Best Screenplay - 14.4% edge, $150 EV, 7.2% Kelly, Liq: 8/10
3. **✅ BET YES @ $0.096** - Sinners Best Costume Design - 14.4% edge, $150 EV, 7.2% Kelly, Liq: 6/10
4. **✅ BET YES @ $0.096** - Hamburger SV relegated - 14.3% edge, $150 EV, 7.1% Kelly, Liq: 2/10
5. **✅ BET YES @ $0.095** - Hamnet Best Adapted Screenplay - 14.2% edge, $150 EV, 7.1% Kelly, Liq: 8/10

📊 **[View Full Edge List (Live Sheet)](https://docs.google.com/spreadsheets/d/1oFnr0HY5jQVzpZzAGwq0EVuzkSR5HJxn0bow_u_pFg8/edit#gid=559016515)**

---

## 📈 System Stats
- **Markets Analyzed:** 7,323 markets tracked
- **Edges Found:** 117 opportunities (0 HIGH, 84 MEDIUM, 33 LOW priority)
- **Update Frequency:** Every hour
- **Last Updated:** 2026-02-10 21:27 EST

---

## 🔍 Advanced Edge Detection Methodology

### **v2.0 New Features:**

**1. Expected Value (EV) Calculation**
- True profit expectation per $1 bet
- Formula: `EV = (P_win × Payout) - (P_loss × Cost)`
- Uses market-implied probabilities adjusted for mispricing

**2. Kelly Criterion Position Sizing**
- Optimal bet size as % of bankroll
- Formula: `Kelly % = Edge / Odds` (capped at 25%)
- Conservative sizing to prevent overbetting

**3. Liquidity Score (1-10 scale)**
- Can you actually get filled at this price?
- Factors: Volume/Liquidity ratio, absolute liquidity depth
- A-grade (8-10): High confidence fills
- F-grade (1-2): Very risky, may not fill

**4. Market Grouping**
- Automatically detects related markets (e.g., Oscar categories, election ranges)
- Groups by 60%+ question similarity
- Helps identify arbitrage across related outcomes

**5. Arbitrage Detection**
- Flags markets where probabilities don't sum correctly
- "POTENTIAL ARB" when YES + NO < 0.98 (accounting for fees)
- "Undervalued" for multi-outcome mispricing

---

## 📊 Output Columns

**Edge Candidates Sheet:**
- **ACTION** - Clear signal: ✅ BET, 🔥 BET NOW, ⚠️ WATCH, 📊 MONITOR
- **BET SIDE** - YES or NO
- **ENTRY** - Current market price
- **FAIR** - Calculated fair value
- **EDGE %** - Percentage edge over fair value
- **EV ($)** - Expected value per $100 bet
- **KELLY %** - Recommended position size
- **LIQ SCORE** - Liquidity rating (1-10)
- **PRIORITY** - HIGH/MEDIUM/LOW
- **MARKET QUESTION** - Full market text
- **GROUP** - Category (Sports, Politics, Crypto, Finance, Other)
- **ARB FLAG** - Edge type (Undervalued, Normalized, or blank)
- **VOLUME** - 24h trading volume
- **LIQUIDITY** - Current order book depth
- **URL** - Direct Polymarket link

**Sorted by:** `EV × Liquidity Score` = **Actually Tradeable Profit**

---

## 🎲 How to Use This Data

### **Quick Decision Framework:**

**HIGH Priority + Liq Score 8-10:** 
- Bet immediately at recommended Kelly %
- High confidence in edge and execution

**MEDIUM Priority + Liq Score 6-7:**
- Bet at 50% of Kelly % (more conservative)
- Good edge but execution risk

**LOW Priority or Liq Score <5:**
- Watch only, don't bet
- Edge exists but too risky to execute

### **Risk Management:**

1. **Never exceed Kelly %** - it's already aggressive
2. **Reduce size for Liq Score <6** - harder to fill
3. **Check ARB FLAG** - "POTENTIAL ARB" = safer bets
4. **Group awareness** - don't over-allocate to one event group

---

## 🛠️ Technical Implementation

**Edge Detection Logic:**
```python
# Fair value estimation
if price < 0.15 and opposite_price > 0.85:
    fair_value = min(1 - opposite_price + 0.05, price * 2.5)
else:
    fair_value = price * 1.5

# Expected Value
payout = (1 / price) - 1
ev = (fair_value × payout) - (1 - fair_value) × 1

# Kelly Criterion
kelly_pct = (edge_pct / 100) / ((1 / price) - 1)
kelly_pct = min(kelly_pct × 100, 25)  # Cap at 25%

# Liquidity Score
if liquidity >= $10K and volume >= $100K: Score = A (9-10)
if liquidity >= $5K and volume >= $50K: Score = B (7-8)
if liquidity >= $2K: Score = C (5-6)
if liquidity >= $500: Score = D (3-4)
else: Score = F (1-2)
```

---

## 🚀 Repository Contents

- `polymarket_edge_analyzer__sheet_updater.py` - Advanced edge detection script
- Reads Sheet1 markets (7,323 total)
- Analyzes with EV, Kelly, Liquidity, Grouping, Arb detection
- Writes to Edge Candidates sorted by tradeable profit

---

## ⏰ Automation

**Trigger:** @trigger:hourly-polymarket-edge-detector
**Frequency:** Every hour (top of the hour)
**Platform:** Nebula workflow automation
**Updates:** Google Sheet + GitHub README automatically

---

## 📖 Version History

**v2.0 (2026-02-10):**
- Added Expected Value calculation
- Added Kelly Criterion position sizing
- Added Liquidity Score (1-10)
- Added Market Grouping
- Added Arbitrage Detection
- Changed sorting to EV × Liquidity Score

**v1.0 (2026-02-10):**
- Basic edge detection using liquidity/volume imbalance
- Simple edge % calculation

---

*Last scan: 2026-02-10 21:27 EST | Next scan: 2026-02-10 22:00 EST*