# Polymarket Edge Detector v3.0

**Multi-Strategy Edge Detection System** - analyzes Polymarket markets hourly with 6 detection methods.

## 🎯 Latest Edges (Updated Hourly)

**887 opportunities identified** from 1,239 active markets analyzed

### Edge Type Breakdown:
- **Lottery Fade:** 755 edges (85.1%) - Extreme longshots overpriced
- **Liquidity Imbalance:** 103 edges (11.6%) - Volume/Liquidity ratio signals
- **Favorite Fade:** 29 edges (3.3%) - Heavy favorites underpricing tail risk
- **Pure Arbitrage:** 0 edges (0.0%) - Risk-free profit opportunities

### Top 3 Opportunities:

**1. Trump deport 250K-500K by Jan 2026?**
- **Edge Type:** Liquidity Imbalance
- **Action:** ✅ BET YES @ $0.904
- **Fair Value:** $1.808
- **Edge:** 100.0% | **EV:** $100 per $100 bet | **Kelly:** 25.0%
- **Reasoning:** Volume/Liquidity ratio 505x - High trading activity suggests market undervaluing YES
- **Volume:** $505,002 | **Liquidity:** $1,000
- **[Trade Now ↗](https://polymarket.com)**

**2. Harvey Weinstein 10-20yr sentence?**
- **Edge Type:** Liquidity Imbalance
- **Action:** ❌ BET NO @ $0.895
- **Fair Value:** $1.790
- **Edge:** 100.0% | **EV:** $100 per $100 bet | **Kelly:** 25.0%
- **Reasoning:** Volume/Liquidity ratio 477x - High trading activity suggests market undervaluing NO
- **Volume:** $477,111 | **Liquidity:** $1,000
- **[Trade Now ↗](https://polymarket.com)**

**3. SCOTUS sports gambling case 2025?**
- **Edge Type:** Liquidity Imbalance
- **Action:** ✅ BET YES @ $0.335
- **Fair Value:** $0.670
- **Edge:** 100.0% | **EV:** $100 per $100 bet | **Kelly:** 25.0%
- **Reasoning:** Volume/Liquidity ratio 276x - High trading activity suggests market undervaluing YES
- **Volume:** $276,166 | **Liquidity:** $1,000
- **[Trade Now ↗](https://polymarket.com)**

📊 **[View Full Edge List (Live Sheet)](https://docs.google.com/spreadsheets/d/1oFnr0HY5jQVzpZzAGwq0EVuzkSR5HJxn0bow_u_pFg8/edit#gid=559016515)**

---

## 📈 System Stats
- **Total Markets:** 7,323 markets in Polymarket
- **Markets Analyzed:** 1,239 active markets
- **Edges Found:** 887 opportunities
- **Update Frequency:** Every hour
- **Last Updated:** 2026-02-11 04:00 UTC

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
- **REASONING** - Why this is an edge
- **VOLUME** - 24h trading volume
- **LIQUIDITY** - Current liquidity depth

---

## 🎲 Risk Management

### Position Sizing (Kelly Criterion):
- **HIGH edges (>20%):** Full Kelly % recommended
- **MEDIUM (10-20%):** 50% of Kelly
- **LOW (<10%):** Watch only, research first

### Liquidity Scores:
- **A (9-10):** Excellent - Trade full size
- **B (7-8):** Good - Trade 75% size
- **C (5-6):** Fair - Trade 50% size
- **D (3-4):** Poor - Trade 25% size or skip
- **F (1-2):** Very Poor - Avoid

---

## 🚀 How to Use

1. **Check Edge Candidates Sheet** - Sorted by Priority + Edge %
2. **Filter by Priority** - Start with HIGH, then MEDIUM
3. **Review Reasoning** - Understand why it's an edge
4. **Check Liquidity Score** - Ensure tradability
5. **Size Position** - Use Kelly % as guide
6. **Execute Trade** - Click market link to trade

---

## 🔗 Links

- **[Live Google Sheet (Edge Candidates)](https://docs.google.com/spreadsheets/d/1oFnr0HY5jQVzpZzAGwq0EVuzkSR5HJxn0bow_u_pFg8/edit#gid=559016515)**
- **[GitHub Repository](https://github.com/dutchiono/polymarket-edge-detector)**
- **[Polymarket](https://polymarket.com)**

---

## 📝 Methodology Notes

- **Sampling:** For performance, system samples 2,000 of 7,323 total markets per scan
- **Active Markets:** Only analyzes markets with >$1K liquidity and recent activity
- **Fair Value:** Calculated using cross-market analysis, liquidity flows, and historical patterns
- **Kelly %:** Conservative sizing (25% max) to account for model uncertainty
- **Liquidity Score:** Based on depth, spread, and recent trading volume

---

## ⚠️ Disclaimer

This system identifies potential market inefficiencies for informational purposes only. Not financial advice. Always do your own research before trading. Past edges do not guarantee future performance.

---

**Built with:** Python, Google Sheets API, Polymarket Gamma API, Nebula AI
**Updates:** Hourly (top of the hour)
**Version:** 3.0 (Multi-Strategy Detection System)
