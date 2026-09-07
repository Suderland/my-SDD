#!/usr/bin/env python3
"""Zero-dependency installer/updater for my-SDD."""
from __future__ import annotations
import argparse
import json
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
VERSION = (REPO / "VERSION").read_text(encoding="utf-8").strip()
LOCK = ".my-sdd.json"

def copy_tree(src: Path, dst: Path):
    if not src.exists():
        return
    for p in src.rglob('*'):
        rel = p.relative_to(src)
        out = dst / rel
        if p.is_dir():
            out.mkdir(parents=True, exist_ok=True)
        else:
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, out)

def install(target: Path, backend: bool, frontend: bool, update: bool=False):
    target = target.resolve()
    target.mkdir(parents=True, exist_ok=True)
    specs = target / '.agents' / 'specs'
    specs.mkdir(parents=True, exist_ok=True)

    # Framework-owned files only. Never touch specs.
    shutil.copy2(REPO / 'AGENTS.md', target / 'AGENTS.md')
    skills_dst = target / '.agents' / 'skills'
    skills_dst.mkdir(parents=True, exist_ok=True)
    copy_tree(REPO / '.agents' / 'skills', skills_dst)
    if backend:
        copy_tree(REPO / 'packs' / 'backend' / 'skills', skills_dst)
    if frontend:
        copy_tree(REPO / 'packs' / 'frontend' / 'skills', skills_dst)

    lock = {
        'version': VERSION,
        'packs': {'backend': backend, 'frontend': frontend},
        'managed': ['AGENTS.md', '.agents/skills/'],
        'preserved': ['.agents/specs/']
    }
    (target / LOCK).write_text(json.dumps(lock, indent=2) + '\n', encoding='utf-8')
    print(f"{'Updated' if update else 'Initialized'} my-SDD {VERSION} in {target}")
    print(f"Packs: backend={backend}, frontend={frontend}")
    print(f"Preserved project Specs: {specs}")

def read_lock(target: Path):
    path = target / LOCK
    if not path.exists():
        raise SystemExit(f"{path} not found. Run init first.")
    return json.loads(path.read_text(encoding='utf-8'))

def main():
    ap=argparse.ArgumentParser(prog='my_sdd.py')
    sub=ap.add_subparsers(dest='cmd', required=True)
    p=sub.add_parser('init')
    p.add_argument('target')
    p.add_argument('--backend', action='store_true')
    p.add_argument('--frontend', action='store_true')
    p=sub.add_parser('update')
    p.add_argument('target')
    p=sub.add_parser('status')
    p.add_argument('target')
    args=ap.parse_args()
    target=Path(args.target)
    if args.cmd=='init':
        install(target,args.backend,args.frontend)
    elif args.cmd=='update':
        lock=read_lock(target)
        packs=lock.get('packs',{})
        install(target,bool(packs.get('backend')),bool(packs.get('frontend')),update=True)
    else:
        lock=read_lock(target)
        print(json.dumps(lock,indent=2))
        specs=target/'.agents'/'specs'
        count=len(list((specs/'features').glob('*/STATE.json'))) if (specs/'features').exists() else 0
        print(f"Feature Specs: {count}")

if __name__=='__main__':
    main()
