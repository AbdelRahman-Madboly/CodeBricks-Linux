# Incident Report — 2024-03-15

**Severity:** HIGH
**Status:** RESOLVED
**Reporter:** Tomás Reyes (DevOps)

## Summary

At 03:42 UTC the inference engine returned 503 errors for all requests.
Root cause: the model worker process was killed by the OOM killer after
GPU memory spiked to 48GB during a batch of 512-token prompts.

## Timeline

- 03:42 UTC — First 503 alert fired in PagerDuty
- 03:44 UTC — Tomás woke up (unhappy)
- 03:51 UTC — Identified OOM kill in /var/log/syslog
- 04:02 UTC — Reduced max_batch_tokens from 8192 to 2048 in config.yaml
- 04:03 UTC — Restarted worker. Service restored.
- 04:05 UTC — Tomás went back to sleep (still unhappy)

## Root Cause

config.yaml had max_batch_tokens set to 8192. A single client sent 64 concurrent
requests each with 512-token prompts. Total: 32768 tokens in one batch.
The model tried to allocate a 48GB attention matrix. The kernel said no.

## Fix

Set max_batch_tokens: 2048 in config.yaml.
Added a per-client rate limit of 10 req/s in nginx.conf.

## Action Items

- [ ] Add memory monitoring alert at 80% GPU usage (assigned: Tomás)
- [ ] Add client-side rate limiting to the SDK (assigned: Priya)
- [ ] Document the max_batch_tokens setting in the API docs (assigned: Marcus)
- [ ] Buy Tomás a coffee (assigned: everyone)
