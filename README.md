# Precedent Needle

> Two cases can look different on the surface and still deserve the same rule.

## Casebook folio

**Policy authority.** The casebook owner freezes a public policy and a short list of material comparison dimensions.

**Recorded precedent.** The owner registers an active public decision and its `ALLOW` or `DENY` outcome. Registration is a declaration, not an authenticity claim.

**Needle test.** A proposer submits a current case from a third origin and states the intended outcome. The named auditor triggers validator review. Validators fetch all three records, hash their bytes, and partition every frozen dimension into materially same or different.

The model never decides consistency. Contract code does:

```text
different dimension exists -> CONSISTENT (precedent distinguished)
all dimensions same + same outcome -> CONSISTENT
all dimensions same + different outcome -> INCONSISTENT
```

The proposer may align one inconsistent outcome to the precedent. An abandoned pending comparison expires permissionlessly. Precedents can be retired only by the casebook owner, without rewriting historical comparisons.

## Reproduce the folio

1. Lint: `$env:PYTHONIOENCODING='utf-8'; genvm-lint contracts/contract.py`
2. Test: `python -m pytest -q`
3. Deploy the exact source: `python scripts/deploy.py`
4. Run the recorded comparison: `python scripts/smoke.py`

All fixture records and demo wallets are controlled by one operator. Distinct addresses and hosts demonstrate authorization and source attribution only.
