# Polymarket Edge Detector

**Automated edge detection system** scanning 7,300+ Polymarket markets hourly for mispricing opportunities.

## 🎯 Latest Edges (Updated Hourly)

**86 opportunities identified** - sorted by edge % (highest profit potential first)

### Top 3 Edges Right Now:
1. **BET NO @ $0.096** - 150% edge - Trump deportation 250K-500K range
2. **BET YES @ $0.028** - 150% edge - Trump deportation 500K-750K range  
3. **BET YES @ $0.015** - 150% edge - Trump deportation 750K-1M range

📊 **[View Full Edge List (Live Sheet)](https://docs.google.com/spreadsheets/d/1oFnr0HY5jQVzpZzAGwq0EVuzkSR5HJxn0bow_u_pFg8/edit#gid=559016515)**

---

## 📈 System Stats
- **Markets Analyzed:** 3,046 active markets
- **Total Market Pool:** 7,324 markets tracked
- **Edge Threshold:** 8%+ minimum
- **Update Frequency:** Every hour
- **Last Updated:** 2026-02-11 01:50 EST

---

## 🔍 Edge Detection Logic

The system identifies **liquidity/volume imbalances** - markets with:
- Low liquidity (< $10K) but high volume (> $50K)
- Extreme pricing (< $0.10) suggesting market overreaction
- Minimum 8% calculated edge vs fair value estimate

**Edge Calculation:**
```
Fair Value = Market Price × 2.5 (for low liquidity scenarios)
Edge % = ((Fair Value / Market Price) - 1) × 100
```

---

## 🛠️ How It Works

1. **Data Source:** Google Sheet with all Polymarket markets (Sheet1)
2. **Analysis Script:** Python script filters active markets, calculates edges
3. **Output:** Edge Candidates tab with ACTION-first layout
4. **Automation:** Nebula trigger runs hourly, updates sheet

---

## 📊 Sheet Structure

**Edge Candidates Tab Columns:**
- **ACTION** - Clear instruction: "BET YES @ $0.096"
- **BET SIDE** - YES or NO
- **ENTRY** - Current market price
- **FAIR** - Calculated fair value
- **EDGE %** - Profit potential
- **PRIORITY** - HIGH/MEDIUM based on edge size
- **MARKET QUESTION** - Full question text
- **REASON** - "Imbalance" (liquidity/volume mismatch)
- **VOLUME** - 24h trading volume
- **LIQUIDITY** - Current liquidity depth
- **URL** - Direct link to market

---

## 🚀 Repository Contents

- `polymarket_edge_analyzer__sheet_updater.py` - Main edge detection script
- Reads Sheet1 markets, analyzes for edges, writes to Edge Candidates
- Deployed as Nebula automation script

---

## ⏰ Automation

**Trigger:** Hourly (top of each hour)
**Platform:** Nebula workflow automation
**Sheet:** Updates automatically, no manual intervention required

---

*Last scan: 2026-02-11 01:50 EST | Next scan: 2026-02-11 02:00 EST*