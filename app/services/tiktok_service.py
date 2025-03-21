"""
TikTok API service for interacting with the TikTok Ads API.
Uses the official TikTok Business API Client SDK.

This file is maintained for backward compatibility.
The implementation has been moved to the app.services.tiktok package.
"""
import logging

# Import the new modular implementation
from app.services.tiktok import TikTokService

# For backward compatibility, re-export TikTokService
__all__ = ["TikTokService"]

logging.info("TikTok service module loaded from modular implementation") 