import csv
import os

def load_portfolio():
    """
    Simulates a localized portfolio state dictionary.
    Keys: Ticker Symbols
    Values: Dict detailing purchase metrics [Shares, Average Cost Basis]
    """
    return {
        "AAPL": {"shares": 10, "buy_price": 150.00},
        "MSFT": {"shares": 5, "buy_price": 300.00},
        "GOOGL": {"shares": 8, "buy_price": 110.00},
        "AMZN": {"shares": 12, "buy_price": 125.00}
    }

def fetch_market_prices():
    """
    Simulates mock dynamic live prices. 
    In production environments, replace these static lookups with live api payloads 
    (e.g., requests.get() against financial API endpoints).
    """
    return {
        "AAPL": 175.50,
        "MSFT": 325.00,
        "GOOGL": 108.20,
        "AMZN": 142.10
    }

def calculate_metrics(portfolio, current_prices):
    """Computes total cost metrics, values, and percentage variance metrics."""
    summary_data = []
    total_invested = 0.0
    total_current_value = 0.0
    
    print("\n--- Processing Live Portfolio Data ---")
    print(f"{'Ticker':<8}{'Shares':<8}{'Avg Cost':<12}{'Market Px':<12}{'Total Cost':<12}{'Curr Value':<12}{'Gain/Loss %':<10}")
    print("-" * 78)
    
    for ticker, hold_info in portfolio.items():
        shares = hold_info["shares"]
        buy_price = hold_info["buy_price"]
        market_price = current_prices.get(ticker, 0.0)
        
        # Quantitative structural logic formulations
        total_cost = shares * buy_price
        current_value = shares * market_price
        
        gain_loss_pct = 0.0
        if total_cost > 0:
            gain_loss_pct = ((current_value - total_cost) / total_cost) * 100
            
        total_invested += total_cost
        total_current_value += current_value
        
        print(f"{ticker:<8}{shares:<8}{f'${buy_price:.2f}':<12}{f'${market_price:.2f}':<12}"
              f"{f'${total_cost:.2f}':<12}{f'${current_value:.2f}':<12}{f'{gain_loss_pct:+.2f}%':<10}")
              
        summary_data.append({
            "Ticker": ticker,
            "Shares": shares,
            "Avg Cost": round(buy_price, 2),
            "Market Price": round(market_price, 2),
            "Total Cost": round(total_cost, 2),
            "Current Value": round(current_value, 2),
            "Gain_Loss_Percentage": round(gain_loss_pct, 2)
        })
        
    print("-" * 78)
    net_gain_loss = total_current_value - total_invested
    net_pct = ((total_current_value - total_invested) / total_invested * 100) if total_invested > 0 else 0
    
    print(f"Total Portfolio Cost Basis : ${total_invested:.2f}")
    print(f"Total Market Valuation    : ${total_current_value:.2f}")
    print(f"Net Account Performance    : ${net_gain_loss:+.2f} ({net_pct:+.2f}%)")
    
    return summary_data

def export_summary_to_csv(summary_data, filename="portfolio_summary.csv"):
    """Pipes metrics systematically to an external clean tabular CSV document."""
    try:
        fields = ["Ticker", "Shares", "Avg Cost", "Market Price", "Total Cost", "Current Value", "Gain_Loss_Percentage"]
        
        with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(summary_data)
            
        print(f"\n✅ Success: Data exported to '{os.path.abspath(filename)}'")
    except IOError as e:
        print(f"\n❌ File Handling Error: Failed to write logs out. Details: {e}")

def main():
    portfolio = load_portfolio()
    current_prices = fetch_market_prices()
    summary_data = calculate_metrics(portfolio, current_prices)
    export_summary_to_csv(summary_data)

if __name__ == "__main__":
    main()
