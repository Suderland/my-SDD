import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CLI=ROOT/'scripts'/'my_sdd.py'
STATUS=ROOT/'.agents'/'skills'/'spec-lifecycle'/'scripts'/'spec_status.py'

class InstallerTests(unittest.TestCase):
    def test_init_creates_core_and_empty_specs(self):
        with tempfile.TemporaryDirectory() as td:
            target=Path(td)/'app'
            subprocess.run([sys.executable,str(CLI),'init',str(target)],check=True,capture_output=True,text=True)
            self.assertTrue((target/'AGENTS.md').exists())
            self.assertTrue((target/'.agents/skills/testing/SKILL.md').exists())
            self.assertTrue((target/'.agents/specs').is_dir())
            self.assertEqual(list((target/'.agents/specs').iterdir()),[])

    def test_update_preserves_specs(self):
        with tempfile.TemporaryDirectory() as td:
            target=Path(td)/'app'
            subprocess.run([sys.executable,str(CLI),'init',str(target),'--backend'],check=True,capture_output=True,text=True)
            custom=target/'.agents/specs/custom.md'
            custom.write_text('do not overwrite',encoding='utf-8')
            subprocess.run([sys.executable,str(CLI),'update',str(target)],check=True,capture_output=True,text=True)
            self.assertEqual(custom.read_text(encoding='utf-8'),'do not overwrite')
            lock=json.loads((target/'.my-sdd.json').read_text())
            self.assertTrue(lock['packs']['backend'])

    def test_optional_packs(self):
        with tempfile.TemporaryDirectory() as td:
            target=Path(td)/'app'
            subprocess.run([sys.executable,str(CLI),'init',str(target),'--backend','--frontend'],check=True,capture_output=True,text=True)
            self.assertTrue((target/'.agents/skills/api-design/SKILL.md').exists())
            self.assertTrue((target/'.agents/skills/accessibility/SKILL.md').exists())

class SpecStatusTests(unittest.TestCase):
    def test_generates_index_and_validates_verified_evidence(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            f=root/'.agents/specs/features/AUTH-001'
            f.mkdir(parents=True)
            (f/'STATE.json').write_text(json.dumps({
                'feature':'AUTH-001','name':'Auth','stage':'implementation','requirements':{
                    'REQ-AUTH-001':{'status':'verified','tasks':['TASK-AUTH-001'],'evidence':['unit:test_auth']},
                    'REQ-AUTH-002':{'status':'in_progress','tasks':['TASK-AUTH-002'],'evidence':[]}
                }
            }),encoding='utf-8')
            cp=subprocess.run([sys.executable,str(STATUS),str(root)],capture_output=True,text=True)
            self.assertEqual(cp.returncode,0,cp.stderr)
            text=(root/'.agents/specs/INDEX.md').read_text()
            self.assertIn('1/2 (50%)',text)
            self.assertIn('REQ-AUTH-002',text)

if __name__=='__main__': unittest.main()
