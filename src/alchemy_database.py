import os, pathlib, datetime, json, uuid, hashlib
from typing import Dict, List, Optional, Any, Union
from enum import Enum


class EntityStatus(Enum):
    ACTIVE = 'active'
    DELETED = 'deleted'
    
def parse_datetime(date_str: str) -> Optional[datetime.datetime]:
    """Parse a string format like 'YYYY-MM-DD', ISO 8601 with timezone, or naive dates."""
    if not date_str:
        return None
    
    try:
        # Try standard YYYY-MM-DD (naive datetime parsing is robust enough for this use case)
        year, month, day = map(int, date_str.split('-'))
        
        # Handle ISO 8601 with timezone offset 'YYYY-MM-DDTHH:mmZ' or similar
        iso_parts = list(date_str.replace('T', '').split('+')[:3]) if len(date_str) > 2 else []
        if len(iso_parts) == 4:
            year, month, tz_hour, tz_min = map(int, iso_parts[:3])
            
            # Convert to UTC for consistency with the rest of the codebase (assuming local time or UTC offset logic carried over)
            dt_str = f"{year}-{month}-{day}T{tz_hour:02d}:{tz_min:02d}"
            if tz_minute_string := iso_parts[-1]:  # Only support single timezone string format like 'Z' for Zulu
                try:
                    time_zone = datetime.timezone(datetime.timedelta(hours=tz_hour, minutes=int(tz_minute_string)))
                except ValueError as e:
                    print(f"Error parsing datetime '{date_str}': {e}")
                    return None
            
            # Create a naive date object to parse later (UTC-aware) if needed for comparison logic
            dt = datetime.datetime(year, month, day).replace(tzinfo=time_zone)
            
        elif len(iso_parts) == 3:
            iso_str = ' '.join(iso_parts[:2]) + '+' + iso_parts[-1]
            try:
                # Parse with explicit timezone offset handling if needed for specific formats like '+00:00' or similar variations
                dt = datetime.datetime.strptime(iso_str, "%Y-%m-%dT%H:%M%z") % (datetime.UTC)  # Handle Zulu hour/minute explicitly
            except ValueError as e
