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

## Filed result

The deployed folio lives at `0x35B89Fb8d0ade0dee063Dc38Adb9E4b8dDdCa26d` on StudioNet.

In comparison `MENDING-1791127238`, validators marked all four frozen dimensions materially the same. Contract code therefore treated the proposed `DENY` as `INCONSISTENT`. The proposer aligned it once to the precedent's `ALLOW`, producing a final `CONSISTENT` record in transaction `0x17400c58fea6c84f4f840b773bda6f1cd4f3bf30d935674587c9322ad06d5423`.

The role boundary has its own network proof: `0x8bee106e384366b56642b32d8fe91fc198b057f23fc96d9bd46fcf10392197e5` finalized with the expected `ERROR` when a non-auditor attempted review.

## Reproduce the folio

1. Lint: `$env:PYTHONIOENCODING='utf-8'; genvm-lint contracts/contract.py`
2. Test: `python -m pytest -q`
3. Deploy the exact source: `python scripts/deploy.py`
4. Run the recorded comparison: `python scripts/smoke.py`

All fixture records and demo wallets are controlled by one operator. Distinct addresses and hosts demonstrate authorization and source attribution only.

The deployment, successful folio, expected rejection, and source-binding manifest are kept as separate JSON records for review.
