# AGENTS.md

## Scope

This file applies to `{{SCOPED_PATH}}`. It inherits the repository root `AGENTS.md`.

## Responsibility

Describe what this directory owns and what belongs elsewhere.

## Required context

List the product, architecture, interface, API, data, security, test, or release documents required for work in this directory.

## Structure and reuse

Document the established framework patterns, components, services, helpers, and dependencies to reuse.

## Local boundaries

Record directory-specific security, data, permission, visibility, performance, accessibility, and external-integration rules.

## Rules

- Keep changes inside this directory's responsibility unless the task explicitly crosses a boundary.
- Follow the established architecture and explain any necessary exception in `PLAN.md` and the affected contract.
- Update local tests and documentation when behavior changes.

## Validation

List exact commands and any manual checks required for this directory. Include constraints such as running services, generated caches, target browsers, or test data.

## Definition of done

Define the local completion conditions that supplement the root rules.

## Do not

List concrete bad patterns, forbidden operations, and common mistakes for this directory.
