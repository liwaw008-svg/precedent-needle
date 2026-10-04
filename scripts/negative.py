from pathlib import Path
import json,re,time
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.contracts import actions as ca
R=Path(__file__).parents[1];ROOT=R.parents[3]
def env(name):
 text=(ROOT/'accounts.env').read_text();return re.search(r'^'+re.escape(name)+r'\s*=\s*"?([^"\r\n]+)',text,re.M).group(1).strip()
def calldata(method=None,args=None,kwargs=None):
 out={}
 if method is not None:out['method']=method
 if args:out['args']=args
 if kwargs:out['kwargs']=kwargs
 return out
ca.make_calldata_object=calldata
accounts={i:create_account(account_private_key=env('ACCOUNT_'+str(i)+'_GENLAYER_PRIVATE_KEY')) for i in (2,4)};clients={i:create_client(chain=studionet,account=a) for i,a in accounts.items()};address=json.loads((R/'deployment.json').read_text())['contractAddress'];run=json.loads((R/'network-run.json').read_text());comparison='GUARD-'+str(int(time.time()));url='https://raw.githack.com/liwaw008-svg/precedent-needle/39570dfa8a77edad42af8113b32fe96650594ce6/evidence/current-case.md'
def finalized(who,method,args):
 tx=clients[who].write_contract(address=address,function_name=method,args=args);clients[who].wait_for_transaction_receipt(transaction_hash=tx,wait_until='finalized',retries=180,interval=5000);return str(tx),clients[who].get_transaction(transaction_hash=tx)
open_tx,opened=finalized(2,'open_comparison',[comparison,run['precedentId'],url,'DENY']);open_leader=(opened.get('consensus_data',{}).get('leader_receipt')or[{}])[0];assert open_leader.get('execution_result')=='SUCCESS',opened
bad_tx,bad=finalized(2,'review_comparison',[comparison]);leader=(bad.get('consensus_data',{}).get('leader_receipt')or[{}])[0];result=leader.get('result');message=str(result.get('payload','') if isinstance(result,dict) else result);assert leader.get('execution_result')=='ERROR' and '[EXPECTED]' in message,bad
out={'guard':'only the designated auditor may review','setupTransaction':open_tx,'rejectedTransaction':bad_tx,'consensus':bad.get('result_name'),'execution':leader.get('execution_result'),'expectedMarker':'[EXPECTED]'};(R/'negative-run.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
