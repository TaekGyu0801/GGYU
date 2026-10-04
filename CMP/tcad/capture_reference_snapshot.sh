#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="${1:-.}"
PROJECT_DIR="$(cd "$PROJECT_DIR" && pwd)"
STAMP="$(date +%Y%m%d_%H%M%S)"
OUT_DIR="${2:-$HOME/CMP_REFERENCE_SNAPSHOTS/Copy_x8_$STAMP}"

mkdir -p "$OUT_DIR/files"
MANIFEST="$OUT_DIR/MANIFEST.txt"
HASHES="$OUT_DIR/SHA256SUMS.txt"

{
  echo "CMP Copy x8 reference snapshot"
  echo "captured_at=$(date -Is)"
  echo "host=$(hostname)"
  echo "user=$(whoami)"
  echo "project_dir=$PROJECT_DIR"
  echo "kernel=$(uname -a)"
  echo "PATH=$PATH"
  echo "sdevice=$(command -v sdevice || true)"
  echo "sde=$(command -v sde || true)"
  echo "swb=$(command -v swb || true)"
  echo
  echo "[project top-level]"
  find "$PROJECT_DIR" -maxdepth 1 -type f -printf '%f\n' | sort
} > "$MANIFEST"

# Capture project-level editable text/source files without assuming a single filename.
find "$PROJECT_DIR" -maxdepth 1 -type f \
  \( -name '*.cmd' -o -name '*.par' -o -name '*.tcl' -o -name '*.scm' \
     -o -name '*.dat' -o -name '*.des' \) -print0 \
  | while IFS= read -r -d '' f; do
      cp -p "$f" "$OUT_DIR/files/"
    done

# Capture the exact generated files needed for reproducibility comparison when present.
for f in \
  gtree.dat \
  pp1_dvs.cmd \
  pp6_des.cmd \
  pp6_des.par \
  n1_msh.tdr \
  n6_des.job \
  n6_des.sta \
  n6_des.err \
  n6_des.out
do
  if [[ -f "$PROJECT_DIR/$f" ]]; then
    cp -p "$PROJECT_DIR/$f" "$OUT_DIR/files/$f"
  fi
done

(
  cd "$OUT_DIR/files"
  find . -maxdepth 1 -type f -print0 | sort -z | xargs -0 sha256sum
) > "$HASHES"

{
  echo
  echo "[reference hashes]"
  cat "$HASHES"
  echo
  echo "[n6_des.out tail]"
  if [[ -f "$PROJECT_DIR/n6_des.out" ]]; then
    tail -n 120 "$PROJECT_DIR/n6_des.out"
  else
    echo "n6_des.out not found"
  fi
  echo
  echo "[n6_des.sta]"
  if [[ -f "$PROJECT_DIR/n6_des.sta" ]]; then
    cat "$PROJECT_DIR/n6_des.sta"
  else
    echo "n6_des.sta not found"
  fi
} >> "$MANIFEST"

echo "Reference snapshot created locally:"
echo "  $OUT_DIR"
echo
echo "Important: this snapshot may contain licensed/proprietary Synopsys-derived files."
echo "Do NOT upload the snapshot directory itself to the public GitHub repository."
echo "Only share sanitized hashes/metadata when needed."
