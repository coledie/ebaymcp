#!/usr/bin/env python3
"""
Fixed MCP Server with proper JSON responses
The issue is that your functions are returning strings instead of proper MCP tool results
"""

import asyncio
import json
import sys
import logging
from fastmcp import FastMCP

# Configure logging to avoid interfering with MCP protocol
logging.basicConfig(
    level=logging.ERROR,  # Only log errors to avoid JSON parsing issues
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('ebay_mcp.log')]  # Log to file, not stdout
)
logger = logging.getLogger(__name__)

# Initialize MCP server
mcp = FastMCP("eBay Research Assistant")

# Your existing classes (DatabaseManager, FixedeBayAPI, etc.) go here...
# But the key fix is in the tool functions below

@mcp.tool()
async def track_product_prices(product_name: str, update_frequency: str = "auto") -> dict:
    """
    Track and analyze prices for a collectible product
    
    Args:
        product_name: Name of the MTG product (e.g., "Dominaria United Draft Booster Box")
        update_frequency: "auto" (smart caching) or "force" (immediate update)
    
    Returns:
        dict: Structured price analysis data
    """
    try:
        force_update = update_frequency == "force"
        
        # Your existing analysis logic here...
        # For now, let's return a proper structured response
        
        analysis = {
            "product_name": product_name,
            "data_points": 25,
            "date_range": 30,
            "sold_listings": 15,
            "active_listings": 10,
            "avg_sold_price": 89.99,
            "median_sold_price": 87.50,
            "min_sold_price": 75.00,
            "max_sold_price": 105.00,
            "sold_price_volatility": 8.25,
            "avg_active_price": 92.50,
            "median_active_price": 90.00,
            "min_active_price": 85.00,
            "max_active_price": 110.00
        }
        
        # Return structured data, not a formatted string
        return {
            "success": True,
            "data": analysis,
            "summary": f"Found {analysis['data_points']} listings for {product_name}",
            "recommendation": "Good buying opportunity" if analysis["avg_active_price"] < analysis["avg_sold_price"] * 1.1 else "Monitor for better prices"
        }
        
    except Exception as e:
        logger.error(f"Error tracking prices: {e}")
        return {
            "success": False,
            "error": str(e),
            "product_name": product_name
        }

@mcp.tool()
async def find_arbitrage_opportunities(product_name: str, min_profit_margin: float = 10.0, 
                                     max_investment: float = 1000.0) -> dict:
    """
    Find arbitrage opportunities with detailed profit analysis
    
    Args:
        product_name: Product to analyze
        min_profit_margin: Minimum profit margin percentage required
        max_investment: Maximum amount you're willing to invest
    
    Returns:
        dict: Arbitrage opportunities data
    """
    try:
        # Your existing arbitrage logic here...
        # For now, return structured mock data
        
        opportunities = [
            {
                "buy_price": 85.00,
                "sell_price": 95.00,
                "net_profit": 6.50,
                "roi_percentage": 7.6,
                "confidence_score": 78,
                "estimated_fees": 3.50,
                "buy_source": "eBay Auctions",
                "sell_source": "eBay Buy-It-Now"
            }
        ]
        
        if opportunities:
            best_opp = opportunities[0]
            max_units = int(max_investment / best_opp["buy_price"])
            total_profit = best_opp["net_profit"] * max_units
            
            return {
                "success": True,
                "opportunities_found": len(opportunities),
                "best_opportunity": best_opp,
                "scaled_analysis": {
                    "max_units": max_units,
                    "total_profit": total_profit,
                    "total_investment": max_investment
                },
                "product_name": product_name
            }
        else:
            return {
                "success": True,
                "opportunities_found": 0,
                "message": f"No arbitrage opportunities found for {product_name} with {min_profit_margin}% minimum margin",
                "product_name": product_name
            }
            
    except Exception as e:
        logger.error(f"Error finding arbitrage: {e}")
        return {
            "success": False,
            "error": str(e),
            "product_name": product_name
        }

@mcp.tool()
async def analyze_investment_potential(product_name: str, investment_horizon: str = "medium") -> dict:
    """
    Comprehensive investment analysis for long-term holding
    
    Args:
        product_name: Product to analyze for investment
        investment_horizon: "short" (3-6m), "medium" (6-18m), "long" (1-3y)
    
    Returns:
        dict: Investment analysis data
    """
    try:
        # Your existing investment analysis logic here...
        # Return structured data instead of formatted string
        
        horizon_multiplier = {"short": 0.5, "medium": 1.0, "long": 2.0}.get(investment_horizon, 1.0)
        
        analysis = {
            "product_name": product_name,
            "investment_score": 72.5,
            "risk_level": "Medium",
            "current_avg_price": 89.99,
            "price_trend_pct": 5.2,
            "volatility_pct": 12.8,
            "target_price_6m": 94.50 * horizon_multiplier,
            "target_price_1y": 102.00 * horizon_multiplier,
            "data_points": 150,
            "recommendation": "Buy - Good investment opportunity with solid fundamentals",
            "investment_horizon": investment_horizon
        }
        
        potential_upside = ((analysis["target_price_1y"] - analysis["current_avg_price"]) / analysis["current_avg_price"] * 100)
        
        return {
            "success": True,
            "analysis": analysis,
            "potential_upside_pct": potential_upside,
            "strategy_tips": [
                "Dollar-cost average over 2-3 months" if analysis["volatility_pct"] > 20 else "Consider lump sum investment",
                f"Wait for price dip below ${analysis['current_avg_price'] * 0.95:.2f} for better entry" if analysis["price_trend_pct"] < 0 else "Current pricing appears favorable",
                "High liquidity expected" if analysis["data_points"] > 50 else "Monitor liquidity before large positions"
            ]
        }
        
    except Exception as e:
        logger.error(f"Error analyzing investment: {e}")
        return {
            "success": False,
            "error": str(e),
            "product_name": product_name
        }

@mcp.tool()
async def market_scanner(scan_type: str = "trending", price_range: str = "100-500", 
                        time_period: str = "7d") -> dict:
    """
    Scan the market for opportunities across multiple products
    
    Args:
        scan_type: "trending" (price momentum), "undervalued", "arbitrage", "new_listings"
        price_range: "under100", "100-500", "500-1000", "over1000"
        time_period: "1d", "7d", "30d" for analysis period
    
    Returns:
        dict: Market scan results
    """
    try:
        # Mock data for demonstration - replace with your actual logic
        opportunities = [
            {
                "product": "Dominaria United Draft Booster Box",
                "price": 89.99,
                "metric": 12.5,
                "data": "$89.99 (+12.5% trend)" if scan_type == "trending" else "$89.99 (15.2% ROI)",
                "trend": 12.5 if scan_type == "trending" else None
            },
            {
                "product": "The Brothers War Set Booster Box", 
                "price": 145.00,
                "metric": 8.7,
                "data": "$145.00 (+8.7% trend)" if scan_type == "trending" else "$145.00 (8.7% ROI)",
                "trend": 8.7 if scan_type == "trending" else None
            }
        ]
        
        # Filter by price range
        price_min, price_max = 0, float('inf')
        if price_range == "under100":
            price_max = 100
        elif price_range == "100-500":
            price_min, price_max = 100, 500
        elif price_range == "500-1000":
            price_min, price_max = 500, 1000
        elif price_range == "over1000":
            price_min = 1000
        
        filtered_opportunities = [
            opp for opp in opportunities 
            if price_min <= opp["price"] <= price_max
        ]
        
        return {
            "success": True,
            "scan_type": scan_type,
            "price_range": price_range,
            "time_period": time_period,
            "products_analyzed": 10,
            "opportunities_found": len(filtered_opportunities),
            "opportunities": filtered_opportunities,
            "summary": f"Found {len(filtered_opportunities)} {scan_type} opportunities in ${price_range.replace('-', ' - ')} range"
        }
        
    except Exception as e:
        logger.error(f"Error in market scanner: {e}")
        return {
            "success": False,
            "error": str(e),
            "scan_type": scan_type,
            "price_range": price_range
        }

@mcp.tool()
async def get_portfolio_summary() -> dict:
    """
    Comprehensive portfolio analysis with performance metrics
    
    Returns:
        dict: Portfolio summary data
    """
    try:
        # Mock portfolio data - replace with your actual database queries
        portfolio = {
            "total_invested": 2450.00,
            "current_value": 2680.50,
            "unrealized_pnl": 230.50,
            "unrealized_pnl_pct": 9.4,
            "active_positions": 5,
            "avg_holding_period_days": 120,
            "holdings": [
                {
                    "product_name": "Dominaria United Draft Booster Box",
                    "quantity": 3,
                    "total_cost": 270.00,
                    "current_value": 285.00,
                    "pnl": 15.00,
                    "pnl_pct": 5.6,
                    "holding_days": 90,
                    "purchase_date": "2024-03-01"
                },
                {
                    "product_name": "Modern Horizons 3 Collector Box",
                    "quantity": 1,
                    "total_cost": 380.00,
                    "current_value": 420.00,
                    "pnl": 40.00,
                    "pnl_pct": 10.5,
                    "holding_days": 60,
                    "purchase_date": "2024-04-15"
                }
            ]
        }
        
        if portfolio["active_positions"] > 0:
            best_performer = max(portfolio["holdings"], key=lambda x: x["pnl_pct"])
            worst_performer = min(portfolio["holdings"], key=lambda x: x["pnl_pct"])
            
            return {
                "success": True,
                "portfolio": portfolio,
                "performance": {
                    "best_performer": best_performer,
                    "worst_performer": worst_performer,
                    "overall_status": "Strong performance" if portfolio["unrealized_pnl_pct"] > 10 else "Moderate performance" if portfolio["unrealized_pnl_pct"] > 0 else "Underperforming"
                },
                "recommendations": [
                    "Consider profit-taking on outperformers" if any(h["pnl_pct"] > 25 for h in portfolio["holdings"]) else "Hold current positions",
                    "Portfolio trending well" if portfolio["unrealized_pnl_pct"] > 0 else "Review underperforming assets"
                ]
            }
        else:
            return {
                "success": True,
                "portfolio": {"active_positions": 0},
                "message": "Portfolio is empty. Start by recording some investments!"
            }
            
    except Exception as e:
        logger.error(f"Error getting portfolio summary: {e}")
        return {
            "success": False,
            "error": str(e)
        }

# IMPORTANT: The key fix is ensuring stdout only contains valid JSON
# Remove any print statements or logging to stdout that could interfere

def main():
    """Main function to run the MCP server"""
    try:
        # Ensure no extra output to stdout
        mcp.run()
    except Exception as e:
        # Log errors to file, not stdout
        logger.error(f"Server error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
