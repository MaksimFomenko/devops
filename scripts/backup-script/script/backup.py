#!/usr/bin/env python3

import argparse
from datetime import datetime, timedelta
from pathlib import Path
import tarfile
import sys

parser = argparse.ArgumentParser(description="Backup script")
parser.add_argument("--source-dir", type=Path, required=True, help="Directory to backup")
parser.add_argument("--archive-dir", type=Path, required=True, help="Directory to store backup archives")
args = parser.parse_args()

source_dir = args.source_dir
archive_dir = args.archive_dir

if not source_dir.is_dir():
    print(f"Error: Source directory {source_dir} does not exist or is not a directory.")
    sys.exit(1)
    
archive_dir.mkdir(parents=True, exist_ok=True)

current_time = datetime.now()
time_str = current_time.strftime("%Y-%m-%d_%H-%M-%S")
cutoff_date = current_time - timedelta(days=7)
archive_path = archive_dir / f"backup_{time_str}.tar.gz"

try:
    with tarfile.open(archive_path, "w:gz") as archive:
        archive.add(source_dir, arcname=source_dir.name)
    print(f"Backup of {source_dir} created at {archive_path}")

    for archive in archive_dir.glob("*.tar.gz"):
        if archive.is_file():
            archive_time = datetime.fromtimestamp(archive.stat().st_mtime)
            if archive_time < cutoff_date:
                archive.unlink()
                print(f"Old backup removed: {archive}")

except (OSError, tarfile.TarError) as e:
    print(f"Error during backup operation: {e}")
    sys.exit(1)

sys.exit(0)