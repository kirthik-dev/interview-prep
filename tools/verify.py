#!/usr/bin/env python3
"""Static integrity and selected runnable-example checks (stdlib only)."""
from html.parser import HTMLParser
from pathlib import Path
import ast, contextlib, io, re
from content import SECTIONS
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.links=[]; self.assets=[]; self.qas=0; self.codes=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='a':self.links.append(a.get('href',''))
        if tag=='script' and 'src' in a:self.assets.append(a['src'])
        if tag=='link' and a.get('rel') in ('stylesheet','icon'):self.assets.append(a['href'])
        if tag=='details' and a.get('class')=='qa':self.qas+=1
html=(ROOT/'index.html').read_text(); page=Page(); page.feed(html)
assert len(page.ids)==len(set(page.ids)), 'Duplicate HTML ids'
for href in page.links:
    if href.startswith('#'):assert href[1:] in page.ids, f'Broken anchor {href}'
    elif href.startswith('./'):assert (ROOT/href[2:]).exists(), f'Missing local link {href}'
for asset in page.assets:assert asset.startswith('./') and (ROOT/asset[2:]).exists(), f'Bad relative asset {asset}'
assert page.qas==sum(len(s['cards']) for s in SECTIONS)
for section in SECTIONS:
    for card in section['cards']:
        for field in ['title','plain','example','short','detailed','follow','mistake','evidence']:
            assert card[field].strip(), (section['id'],field)
        code=card.get('code')
        if code and not code.startswith(('SELECT','WITH','MERGE','--')):ast.parse(code)
# Verify actual examples, not merely that the snippets exist.
expected={
 ('ylogx',0):"[{'amount': -2}]",
 ('python',0):'[3]\n[2]',
 ('python',1):'12.5',
 ('python',2):'50',
 ('python',3):'15',
 ('cdc-scd',1):'update 1\ndelete 2\ninsert 3',
 ('ml',2):'[None, 10, 20, 30]\n[None, None, 15.0, 25.0]',
 ('ml',4):'3.0 0.2'
}
for (sid,i),want in expected.items():
    code=next(s for s in SECTIONS if s['id']==sid)['cards'][i]['code']
    out=io.StringIO()
    with contextlib.redirect_stdout(out):exec(compile(code,'<example>','exec'),{})
    assert out.getvalue().strip()==want, (sid,i,out.getvalue())
# Guard the intentional distinction between inspected code and proposed/practice content.
for phrase in ['Iceberg','Proposed design','EventHubConsumerClient','baseline','customer_unique_id','40%','50+','12%','version','MLflow']:
    assert phrase in html, phrase
# Secret/contact patterns in all files eligible for publication. Never print a matching line.
patterns=[r'github_pat_[A-Za-z0-9_]{20,}',r'gh[pousr]_[A-Za-z0-9]{20,}',r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?:com|org|net|in|io)\b',r'\b[0-9]{10}\b',r'AccountKey=[A-Za-z0-9+/=]{20,}']
for file in ROOT.rglob('*'):
    if not file.is_file() or '.git' in file.parts or '__pycache__' in file.parts or file.suffix in ('.zip','.png','.pyc'):continue
    text=file.read_text(errors='replace')
    assert not any(re.search(p,text) for p in patterns), f'Credential/contact pattern detected in {file.relative_to(ROOT)}'
print(f'PASS: {page.qas} complete Q&A; {len(page.ids)} unique IDs; all local links/assets resolve; 8 pure-Python examples match expected outputs; no credential/contact patterns.')
