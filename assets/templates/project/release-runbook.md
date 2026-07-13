# Release runbook

This document describes the release process. It does not authorize a production change.

## Environments

| Environment | Purpose | Source revision | Data boundary | Owner |
|---|---|---|---|---|

## Release inputs

- Expected revision or artifact
- Environment configuration requirements without secret values
- Change and dependency summary
- Migration decision
- Queue, worker, scheduler, cache, or background-job impact
- Required test and manual evidence

## Preflight

List Git, artifact, environment, backup, migration, permission, capacity, and dependency checks.

## Backup and rollback

| Asset | Backup or rollback target | Verification | Retention | Owner |
|---|---|---|---|---|

## Release procedure

List exact commands or operator actions after the environment is known.

## Post-release verification

Check the deployed revision, health, changed APIs or pages, stateful behavior, background work, logs, and user-visible paths affected by the release.

## Stop conditions

List technical blockers, failed health or migration checks, missing backups, uncertain revision, and owner `NO_GO` conditions.

## Evidence record

Record timestamps, revision, commands, results, manual checks, unresolved risks, and the rollback target used for this release.
