#!/usr/bin/env python3
"""
Heska Agent - Main Loop
Monitors meme coin narratives and sends Telegram alerts
"""

import time
import logging
from datetime import datetime
from config import Config
from sources.sharpe import SharpeNarratives
from sources.lunarcrush import LunarCrush
from sources.xscanr import XScanr
from alerts.telegram import TelegramBot

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - Heska - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class HeskaAgent:
    """
    Main Heska agent that monitors meme coin narratives
    """
    
    def __init__(self):
        self.config = Config()
        self.sharpe = SharpeNarratives(self.config.sharpe_api_key)
        self.lunar = LunarCrush(self.config.lunarcrush_api_key)
        self.xscanr = XScanr()
        self.telegram = TelegramBot(
            self.config.telegram_token,
            self.config.telegram_chat_id
        )
        
        self.last_sector_state = "UNKNOWN"
        self.tracked_coins = set()
        
        logger.info("🚀 Heska Agent initialized")
    
    def check_narrative_heat(self):
        """
        Check if memecoins narrative sector is heating up
        """
        try:
            narrative_data = self.sharpe.get_memecoins_narrative()
            
            if not narrative_data:
                return None
            
            # Simple logic: compare current vs baseline
            momentum = narrative_data.get('momentum', 0)
            social_volume = narrative_data.get('social_volume', 0)
            
            if momentum > 1.5 and social_volume > self.config.social_threshold:
                state = "HOT"
            elif momentum > 1.2:
                state = "WARMING"
            else:
                state = "COOL"
            
            # Alert if state changed
            if state != self.last_sector_state and state in ["HOT", "WARMING"]:
                self.telegram.send_alert(
                    f"🔥 Heska | MEMECOINS {state}\n"
                    f"Momentum: {momentum:.2f}x | Social volume rising\n"
                    f"Sharpe shows memecoins narrative heating up."
                )
                logger.info(f"Sector state changed: {self.last_sector_state} → {state}")
            
            self.last_sector_state = state
            return state
            
        except Exception as e:
            logger.error(f"Error checking narrative heat: {e}")
            return None
    
    def find_hot_coins(self):
        """
        Find coins with exploding social metrics
        """
        try:
            trending = self.lunar.get_trending_coins(category='memecoins')
            
            for coin in trending[:5]:  # Top 5 only
                ticker = coin.get('symbol', 'UNKNOWN')
                social_spike = coin.get('social_volume_24h_change', 0)
                
                # If social volume spiked >100% and we haven't alerted yet
                if social_spike > 100 and ticker not in self.tracked_coins:
                    self.telegram.send_alert(
                        f"🆕 Heska | NEW HOT MEME: ${ticker}\n"
                        f"Social volume +{social_spike:.0f}% in 24h\n"
                        f"Contributors surging | Trend: UP\n"
                        f"Check liquidity and holder distribution before entering."
                    )
                    self.tracked_coins.add(ticker)
                    logger.info(f"New hot coin detected: ${ticker}")
            
        except Exception as e:
            logger.error(f"Error finding hot coins: {e}")
    
    def scan_new_launches(self):
        """
        Scan for new influencer-driven meme launches
        """
        try:
            launches = self.xscanr.get_recent_launches(chain='solana', hours=1)
            
            for launch in launches:
                ticker = launch.get('ticker', 'UNKNOWN')
                influencer = launch.get('influencer_handle', 'Unknown')
                followers = launch.get('followers', 0)
                mc = launch.get('market_cap', 0)
                liq = launch.get('liquidity', 0)
                tweet_url = launch.get('tweet_url', '')
                
                # Only alert for influencers with 50k+ followers
                if followers > 50000 and ticker not in self.tracked_coins:
                    self.telegram.send_alert(
                        f"⚡ Heska | NEW SOL MEME: ${ticker}\n"
                        f"From @{influencer} ({followers/1000:.0f}k followers)\n"
                        f"MC: ${mc/1000:.0f}k | Liq: ${liq/1000:.0f}k\n"
                        f"Tweet: {tweet_url}"
                    )
                    self.tracked_coins.add(ticker)
                    logger.info(f"New launch detected: ${ticker} from @{influencer}")
            
        except Exception as e:
            logger.error(f"Error scanning launches: {e}")
    
    def run(self):
        """
        Main monitoring loop
        """
        logger.info("👁️ Heska is now watching...")
        self.telegram.send_alert("🚀 Heska Agent started - monitoring meme narratives")
        
        while True:
            try:
                logger.info("=== Heska scan cycle ===")
                
                # 1. Check sector-level narrative heat
                self.check_narrative_heat()
                
                # 2. Find trending coins with social spikes
                self.find_hot_coins()
                
                # 3. Scan for new influencer launches
                self.scan_new_launches()
                
                # Wait before next cycle
                wait_time = self.config.scan_interval_minutes * 60
                logger.info(f"Sleeping for {self.config.scan_interval_minutes} minutes...")
                time.sleep(wait_time)
                
            except KeyboardInterrupt:
                logger.info("🛑 Heska shutting down...")
                self.telegram.send_alert("🛑 Heska Agent stopped")
                break
            except Exception as e:
                logger.error(f"Error in main loop: {e}")
                time.sleep(60)  # Wait 1 min on error

if __name__ == "__main__":
    heska = HeskaAgent()
    heska.run()
