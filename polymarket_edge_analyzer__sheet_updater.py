"""
Polymarket Edge Analyzer - Sheet Updater
Reads all markets from Sheet1, analyzes for edges, writes to Edge Candidates tab
"""

def transform(data, context):
    import ast
    
    # Get sheet data from context (passed by run_action for google_sheets)
    sheet_data = context.get('sheet_data', [])
    
    if not sheet_data or len(sheet_data) < 2:
        return {
            'error': 'No sheet data provided',
            'edges': [],
            'total_analyzed': 0
        }
    
    headers = sheet_data[0]
    rows = sheet_data[1:]
    
    # Column mapping
    col_idx = {h: i for i, h in enumerate(headers)}
    
    edges = []
    analyzed = 0
    
    for row in rows:
        if len(row) < len(headers):
            continue
        
        try:
            market_question = row[col_idx['market_question']]
            outcome_prices_str = row[col_idx['outcome_prices']]
            volume = float(row[col_idx['volume']]) if row[col_idx['volume']] else 0
            liquidity = float(row[col_idx['liquidity']]) if row[col_idx['liquidity']] else 0
            url = row[col_idx['url']]
            active = row[col_idx['active']]
            closed = row[col_idx['closed']]
            
            # Skip inactive/closed
            if active != 'TRUE' or closed != 'FALSE':
                continue
            
            # Parse prices
            prices = ast.literal_eval(outcome_prices_str)
            yes_price = float(prices[0])
            no_price = float(prices[1])
            
            # Skip extreme prices or low volume
            if yes_price == 0 or yes_price == 1 or no_price == 0 or no_price == 1:
                continue
            if volume < 500:
                continue
            
            analyzed += 1
            
            # Edge detection: low liquidity + high volume = potential mispricing
            if liquidity > 0 and liquidity < 10000 and volume > 50000:
                # YES edge
                if yes_price < 0.1:
                    fair_yes = yes_price * 2.5
                    edge_pct = ((fair_yes / yes_price) - 1) * 100
                    if edge_pct >= 8:
                        edges.append({
                            'action': f"BET YES @ ${yes_price:.3f}",
                            'bet_side': 'YES',
                            'entry_price': yes_price,
                            'fair_value': fair_yes,
                            'edge_pct': edge_pct,
                            'priority': 'HIGH' if edge_pct >= 20 else 'MEDIUM',
                            'market_question': market_question,
                            'volume': volume,
                            'liquidity': liquidity,
                            'url': url
                        })
                
                # NO edge
                if no_price < 0.1:
                    fair_no = no_price * 2.5
                    edge_pct = ((fair_no / no_price) - 1) * 100
                    if edge_pct >= 8:
                        edges.append({
                            'action': f"BET NO @ ${no_price:.3f}",
                            'bet_side': 'NO',
                            'entry_price': no_price,
                            'fair_value': fair_no,
                            'edge_pct': edge_pct,
                            'priority': 'HIGH' if edge_pct >= 20 else 'MEDIUM',
                            'market_question': market_question,
                            'volume': volume,
                            'liquidity': liquidity,
                            'url': url
                        })
        
        except Exception:
            continue
    
    # Sort by edge %
    edges.sort(key=lambda x: x['edge_pct'], reverse=True)
    
    # Format for Google Sheets
    rows_output = [[
        "ACTION", "BET SIDE", "ENTRY", "FAIR", 
        "EDGE %", "PRIORITY", "MARKET QUESTION", "REASON", 
        "VOLUME", "LIQUIDITY", "URL"
    ]]
    
    for edge in edges:
        rows_output.append([
            edge['action'],
            edge['bet_side'],
            edge['entry_price'],  # Raw number for proper column width
            edge['fair_value'],    # Raw number for proper column width
            edge['edge_pct'],      # Raw number for sorting
            edge['priority'],
            edge['market_question'],
            "Imbalance",  # Simplified reasoning
            edge['volume'],
            edge['liquidity'],
            edge['url']
        ])
    
    return {
        'rows': rows_output,
        'total_analyzed': analyzed,
        'edges_found': len(edges),
        'success': True
    }
