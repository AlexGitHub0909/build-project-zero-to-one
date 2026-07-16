# Frontend rules

## Load when

Load this reference for an interactive web, mobile, or desktop interface. A project may need both website and frontend rules when it combines public content with an application.

## Establish scope

Confirm from product material or the user:

- user roles, primary journeys, supported devices, and interface surfaces;
- navigation, deep-linking, session, offline, and multi-window expectations where relevant;
- the source of truth for remote or shared data, local state, drafts, and cached data;
- accessibility, localization, browser or operating-system support, and performance constraints;
- the existing design system, component library, visual references, and approval owner.

## Rules

- Define each route or screen by purpose, allowed roles, entry points, exits, and observable completion state.
- Use a flow, wireframe, state prototype, visual screen, or clickable prototype when interaction or layout decisions need human confirmation. Include the important loading, empty, error, permission, and recovery states rather than showing only the happy path.
- Cover loading, empty, partial, stale, success, validation, disabled, permission-denied, and recoverable error states where they can occur.
- Reuse established tokens, components, form patterns, navigation, and request helpers before creating local variants.
- Keep authorization on the trusted enforcement boundary. In a client-server system, hidden controls and client-side route guards are not sufficient permission checks.
- Define request ownership, cache lifetime, invalidation, optimistic behavior, retries, cancellation, and stale-response handling before adding another data layer.
- Validate at the user boundary for clear feedback and again at the trusted boundary for correctness. Preserve user input when a recoverable submission fails.
- Treat URLs, browser or device storage, uploaded files, clipboard data, rich text, and rendered HTML as untrusted input. Keep credentials and server secrets out of client bundles and logs.
- Keep semantic structure, keyboard access, focus movement, labels, contrast, target size, reduced motion, and responsive behavior in the definition of done.
- Avoid duplicating server domain rules in presentation code. Keep formatting and display mapping close to the interface, and keep shared business behavior in its canonical layer.

## Evidence

Choose checks that match the interface:

- focused component or view tests for meaningful state transitions;
- route, role, form, and error-path tests;
- type, lint, and build checks required by the selected stack;
- keyboard, accessibility, responsive, and supported-platform checks;
- real request integration or contract fixtures for critical flows;
- target-environment checks when local rendering cannot prove the final behavior.
- comparison with the approved prototype or interaction artifact, with intentional differences recorded.

Put concrete state libraries, component boundaries, styling rules, route conventions, generated-cache constraints, and commands in the relevant scoped `AGENTS.md`.
