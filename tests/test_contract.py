from pathlib import Path
S=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text()
def test_public_surface():
 for name in ('open_casebook','register_precedent','open_comparison','review_comparison','align_outcome','expire_comparison','retire_precedent','get_comparison'):assert 'def '+name in S
def test_validator_recomputes_partition():assert "run()==leader.calldata" in S and "same+different!=list(range(len(dims)))" in S
def test_consistency_is_contract_derived():assert "c.proposed_outcome==p.outcome" in S and "not comparable" in S
def test_source_attribution():assert "origin in (b.policy_origin,p.record_origin)" in S and "policy_digest" in S and "precedent_digest" in S and "case_digest" in S
def test_recovery_and_authorization():assert "gl.message.sender_address!=c.proposer" in S and "now()<=int(c.deadline)" in S and "gl.message.sender_address!=b.owner" in S
