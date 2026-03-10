# Varro Notes Index

Last updated: 2026-03-09.

## Core notes

- [01 Project Map](01_project_map.md)
- [02 App + UI Architecture](02_app_ui_architecture.md)
- [03 Chat + Agent Runtime](03_chat_agent_runtime.md)
- [04 Dashboard Framework](04_dashboard_framework.md)
- [05 Data + Context Pipeline](05_data_context_pipeline.md)
- [06 Playground Exploration](06_playground_exploration.md)
- [07 Deployment](07_deployment.md)

## Dev

- [Dev Loop](dev/loop.md) — Test → Review → Implement cycle
- [Test Plan](dev/test_plan.md) — Questions to test the app with

## Notes

- [Dashboard Filter Select Value Label](notes/dashboard_filter_select_value_label.md)
- [Bubblewrap Phase 0 Preflight](notes/bwrap_phase0_preflight.md)
- [Bubblewrap Phase 2 + 3 Shell Sandbox](notes/bwrap_phase2_phase3_shell_sandbox.md)
- [DEV Bash Absolute Path Translation](notes/dev_bash_absolute_path_translation.md)
- [Playground Q1: Befolkning](notes/playground_q1_befolkning.md) — Chat 70 findings: Snapshot auth failure, exploration quality
- [Playground Q2: Husleje](notes/playground_q2_husleje.md) — Chat 71 findings: Strong session, subject search tool opportunity
- [Playground Q4: Afgrøder](notes/playground_q4_afgroeder.md) — Chat 72 findings: Cleanest session, SQL cast syntax doc gap
- [Playground Q5: Dansk økonomi](notes/playground_q5_oekonomi.md) — Chat 73 findings: Best session, vague question handled perfectly, snapshot fixed
- [Playground Q9: Regioner](notes/playground_q9_regioner.md) — Chat 74 findings: Strongest analysis session, filter value contract gap, parquet type constraint
- [Stripe payments + user balance](notes/stripe_payments_balance.md) — DKK top-up flow, webhook reconciliation, balance column, settings top-up UI
- [Model cost debiting from user balance](notes/model_cost_debiting.md) — Per-run model charge ledger, DKK debits, low-balance gating, hourly price refresh

## Skills

- `$playground-explorer` — Interactive CLI-first trajectory exploration and playground improvement discovery.
- `$analyse-trajectory` — Retrospective audit of completed chats.
- `$findings-to-plan` — Convert playground findings into concrete file-level implementation plans.
- `$implement-findings` — Reads findings from the above skills, maps to code, implements changes, updates findings with status.

## Suggested reading order

1. `01_project_map.md` for the overall map.
2. `02_app_ui_architecture.md` + `03_chat_agent_runtime.md` for runtime behavior.
3. `04_dashboard_framework.md` for dashboard implementation details.
4. `06_playground_exploration.md` for interactive trajectory improvement workflow and skill split.
5. `05_data_context_pipeline.md` for offline data preparation.
