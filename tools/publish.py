#!/usr/bin/env python3
"""Publish without persisting credentials. Token is requested with hidden input."""
import base64, getpass, json, pathlib, sys, time, urllib.request, urllib.error
ROOT = pathlib.Path(__file__).resolve().parents[1]
TOKEN = getpass.getpass('GitHub token (hidden): ')
def api(method, path, payload=None):
    data = None if payload is None else json.dumps(payload).encode()
    req = urllib.request.Request('https://api.github.com'+path, data=data, method=method,
        headers={'Authorization':'Bearer '+TOKEN,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'interview-prep-publisher'})
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            raw=response.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as exc:
        # Do not print request headers or credentials.
        try: message=json.loads(exc.read()).get('message','Request failed')
        except Exception: message='Request failed'
        raise RuntimeError(f'GitHub HTTP {exc.code}: {message}') from None
try:
    user=api('GET','/user')['login']
    print('Authenticated GitHub account:', user, flush=True)
    if user.lower()!='kirthik-dev': raise RuntimeError('Account does not match kirthik-dev. No changes made.')
    print('Waiting for PUBLISH on stdin; no repository changes yet.', flush=True)
    if input().strip()!='PUBLISH': raise RuntimeError('Publication cancelled.')
    repo='kirthik-dev/interview-prep'; endpoint='/repos/'+repo
    try:
        existing=api('GET',endpoint)
        raise RuntimeError('Repository already exists; stopping to protect existing content.')
    except RuntimeError as exc:
        if 'HTTP 404:' not in str(exc): raise
    api('POST','/user/repos',{'name':'interview-prep','description':'Resume, projects, data engineering and MLOps interview study guide','private':False,'auto_init':True})
    print('Created https://github.com/'+repo, flush=True)
    branch=api('GET',endpoint+'/git/ref/heads/main')['object']['sha']
    base_tree=api('GET',endpoint+'/git/commits/'+branch)['tree']['sha']
    tree=[]
    for file in sorted(ROOT.rglob('*')):
        rel=file.relative_to(ROOT)
        if not file.is_file() or any(p in {'.git','__pycache__'} for p in rel.parts) or file.suffix in {'.png','.zip','.pyc'}: continue
        blob=api('POST',endpoint+'/git/blobs',{'content':base64.b64encode(file.read_bytes()).decode(),'encoding':'base64'})
        tree.append({'path':str(rel),'mode':'100644','type':'blob','sha':blob['sha']})
    tree_sha=api('POST',endpoint+'/git/trees',{'base_tree':base_tree,'tree':tree})['sha']
    commit=api('POST',endpoint+'/git/commits',{'message':'Build complete interview study guide','tree':tree_sha,'parents':[branch]})['sha']
    api('PATCH',endpoint+'/git/refs/heads/main',{'sha':commit,'force':False})
    print('Published source commit:',commit,flush=True)
    try:
        pages=api('POST',endpoint+'/pages',{'build_type':'legacy','source':{'branch':'main','path':'/'}})
    except RuntimeError as exc:
        if 'HTTP 409:' not in str(exc): raise
        pages=api('GET',endpoint+'/pages')
    print('Pages configured:',pages.get('html_url','https://kirthik-dev.github.io/interview-prep/'),flush=True)
    for attempt in range(24):
        pages=api('GET',endpoint+'/pages')
        status=pages.get('status')
        print('Pages status:',status,flush=True)
        if status=='built': break
        if status=='errored': raise RuntimeError('Pages build errored; inspect repository Pages settings.')
        time.sleep(10)
    print('Finished. Live site requires an HTTP verification.',flush=True)
except Exception as exc:
    print(str(exc),file=sys.stderr,flush=True)
    sys.exit(1)
finally:
    TOKEN=''
