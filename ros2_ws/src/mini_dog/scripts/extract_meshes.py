#!/usr/bin/env python3
"""Extract the historical quadruped STL assets shipped as a compressed archive.

Run before the first colcon build. No extra Python dependencies are required.
"""
from pathlib import Path
import shutil
import tarfile

PKG_ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = PKG_ROOT / "meshes.tar.xz"
EXPECTED = {
    "meshes/base_link.stl",
    *{f"meshes/leg_{leg}{part}.stl" for leg in range(1, 5) for part in ("", "_2", "_3")},
}


def main():
    if not ARCHIVE.is_file():
        raise SystemExit(f"Missing mesh archive: {ARCHIVE}")
    with tarfile.open(ARCHIVE, "r:xz") as archive:
        members = archive.getmembers()
        names = {member.name for member in members}
        if names != EXPECTED or len(members) != len(EXPECTED):
            raise SystemExit("Unexpected archive entries; refusing extraction")
        for member in members:
            if not member.isfile() or member.size > 10_000_000:
                raise SystemExit(f"Unsafe archive entry: {member.name}")
            out = PKG_ROOT / member.name
            out.parent.mkdir(parents=True, exist_ok=True)
            source = archive.extractfile(member)
            if source is None:
                raise SystemExit(f"Could not read: {member.name}")
            with source, out.open("wb") as dest:
                shutil.copyfileobj(source, dest)
    print(f"Extracted {len(EXPECTED)} STL mesh files to {PKG_ROOT / 'meshes'}")


if __name__ == "__main__":
    main()
