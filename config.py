"""
Heska Agent Configuration
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Configuration class for Heska agent
    """
    
    def __init__(self):
        # API Keys
        self.sharpe_api_key = os.getenv('SHARPE_API_KEY', '')
        self.lunarcrush_api_key = os.getenv('LUNARCRUSH_API_KEY', '')
        
        # Telegram Settings
        self.telegram_token = os.getenv('TELEGRAM_BOT_TOKEN', '')
        self.telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID', '')
        
        # Agent Behavior
        self.scan_interval_minutes = int(os.getenv('SCAN_INTERVAL_MINUTES', '5'))
        self.social_threshold = int(os.getenv('SOCIAL_THRESHOLD', '1000'))
        
        # Chains to monitor (for future expansion)
        self.chains = os.getenv('CHAINS', 'solana').split(',')
        
        # Validate required settings
        self.validate()
    
    def validate(self):
        """
        Validate that required config values are set
        """
        required = [
            ('SHARPE_API_KEY', self.sharpe_api_key),
            ('LUNARCRUSH_API_KEY', self.lunarcrush_api_key),
            ('TELEGRAM_BOT_TOKEN', self.telegram_token),
            ('TELEGRAM_CHAT_ID', self.telegram_chat_id)
        ]
        
        missing = [name for name, value in required if not value]
        
        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing)}\n"
                f"Please create a .env file with these values."
            )
