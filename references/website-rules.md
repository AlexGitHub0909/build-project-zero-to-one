# Website rules

## Load when

Load this reference for public, discoverable, content-led, documentation, campaign, or marketing pages. Do not load it for an internal application solely because the application runs in a browser. Load frontend rules as well when the site includes substantial interactive or signed-in flows.

## Establish scope

Confirm from product material or the user:

- intended audiences and the action each audience should take;
- which pages are public, private, indexable, localized, or time-bound;
- who owns factual claims, content updates, brand assets, and legal text;
- whether forms, analytics, cookies, a CMS, search, or third-party embeds are needed;
- target devices, browsers, accessibility expectations, and performance constraints.

## Rules

- Keep public claims tied to approved product facts and current evidence. Do not advertise planned or partial capabilities as available.
- Define the information architecture, durable URLs, navigation, page purpose, and content owner before polishing isolated sections.
- When structure, visual hierarchy, messaging, or responsive behavior remains ambiguous, present a sitemap, wireframe, visual screen, or clickable prototype for human review before production implementation.
- Add titles, descriptions, canonical URLs, social previews, robots rules, sitemaps, and structured data only where discovery requirements call for them. Keep them consistent with visible content.
- Reuse the project's design system and content patterns. Record responsive behavior, focus order, keyboard access, semantic structure, contrast, and reduced-motion behavior where relevant.
- Give public forms clear validation, success, retry, error, consent, privacy, retention, and abuse-handling behavior.
- Add analytics, cookies, chat, tracking pixels, and external embeds only with user approval and a documented privacy boundary.
- Define HTTPS, redirects, cache behavior, security headers, and third-party origins when the site owns those concerns. Do not weaken browser protections to accommodate an embed without reviewing the exposure.
- Set asset and performance expectations for the critical public path. Avoid large media, unnecessary client code, and third-party requests without a measured reason.
- Keep content source, publication flow, localization ownership, and stale-content checks explicit when more than one person or system can update the site.

## Evidence

Choose checks that match the site:

- route, link, asset, and not-found behavior;
- rendered metadata and indexability rules;
- narrow and wide viewport behavior, keyboard navigation, and accessibility checks;
- critical-page loading and media behavior under realistic network conditions;
- form success, failure, validation, privacy, and abuse paths;
- target-environment checks for the changed public URLs.
- comparison of the implemented page with the approved prototype, including recorded intentional differences.

Put concrete framework commands, supported browsers, content sources, performance budgets, and forbidden patterns in the relevant scoped `AGENTS.md`.
