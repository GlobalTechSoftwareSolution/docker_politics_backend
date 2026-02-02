#!/usr/bin/env python3
"""
Sync local PostgreSQL data to Nhost PostgreSQL
"""
import os
import sys
import subprocess
import json
from pathlib import Path

def run_cmd(cmd, shell=True):
    """Run shell command and return output"""
    result = subprocess.run(cmd, shell=shell, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
        return None
    return result.stdout.strip()

def main():
    print("🚀 Syncing local data to Nhost...")
    
    # Step 1: Dump local data
    print("1. Dumping local data...")
    dump_file = "nhost_data.json"
    cmd = f"python manage.py dumpdata users --indent 2 > {dump_file}"
    if run_cmd(cmd) is None:
        print("❌ Failed to dump data")
        return 1
    
    if not Path(dump_file).exists():
        print("❌ Dump file not created")
        return 1
    
    print(f"✅ Data dumped to {dump_file}")
    
    # Step 2: Get Nhost DB connection (user needs to provide)
    print("\n2. Enter Nhost PostgreSQL connection string:")
    print("Format: postgresql://user:password@host:port/database")
    db_url = input("DB_URL: ").strip()
    
    if not db_url:
        print("❌ No DB URL provided")
        return 1
    
    # Step 3: Load data to Nhost
    print("\n3. Loading data to Nhost...")
    os.environ['DATABASE_URL'] = db_url
    cmd = f"python manage.py loaddata {dump_file}"
    result = run_cmd(cmd)
    
    if result is None:
        print("❌ Failed to load data")
        return 1
    
    print("✅ Data synced successfully!")
    print(f"Loaded from: {dump_file}")
    print(f"To: {db_url}")
    
    # Cleanup
    Path(dump_file).unlink()
    print("🧹 Cleaned up temporary files")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())