#!/usr/bin/env python3
"""Validate my-SDD Skill structure and important repository invariants."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
NAME_RE=re.compile(r'^[a-z0-9-]{1,64}$')

def frontmatter(text):
    if not text.startswith('---\n'):
        return None
    try:
        _, fm, _ = text.split('---',2)
    except ValueError:
        return None
    data={}
    for line in fm.strip().splitlines():
        if ':' in line:
            k,v=line.split(':',1)
            data[k.strip()]=v.strip()
    return data

def main():
    errors=[]
    skills=list(ROOT.glob('.agents/skills/*/SKILL.md'))+list(ROOT.glob('packs/*/skills/*/SKILL.md'))+list(ROOT.glob('maintainer/skills/*/SKILL.md'))
    names=set()
    for p in skills:
        text=p.read_text(encoding='utf-8')
        fm=frontmatter(text)
        if not fm:
            errors.append(f'{p}: missing/invalid frontmatter'); continue
        name=fm.get('name','')
        desc=fm.get('description','')
        if not NAME_RE.match(name): errors.append(f'{p}: invalid name {name!r}')
        if name in names: errors.append(f'{p}: duplicate skill name {name}')
        names.add(name)
        if not desc or len(desc)>1024: errors.append(f'{p}: description missing or >1024 chars')
        if len(text.splitlines())>500: errors.append(f'{p}: SKILL.md exceeds 500 lines')
        if p.parent.name!=name: errors.append(f'{p}: directory/name mismatch')
    # Validate eval JSON
    for p in ROOT.rglob('evals.json'):
        try: json.loads(p.read_text(encoding='utf-8'))
        except Exception as exc: errors.append(f'{p}: invalid JSON: {exc}')
    # Required baseline artifacts
    for rel in ['AGENTS.md','README.md','VERSION','scripts/my_sdd.py','.agents/skills/testing/SKILL.md','.agents/skills/spec-lifecycle/SKILL.md']:
        if not (ROOT/rel).exists(): errors.append(f'missing {rel}')
    if errors:
        print('\n'.join('ERROR: '+e for e in errors), file=sys.stderr)
        return 1
    print(f'OK: {len(skills)} Skills validated; frontmatter/line limits/JSON checks passed.')
    return 0

if __name__=='__main__': raise SystemExit(main())
