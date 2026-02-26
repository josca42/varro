# Dashboard filter-select: value vs label

Trajectory chats 30-31 exposed a recurring failure mode:

- Dashboards used `options="query:regioner"` with SQL returning `SELECT kode, titel`.
- Framework consumed only first column (`.scalars()`), while agent instructions said options queries were single-column.
- Fresh-session agent guessed label values in URL (`region=Region Hovedstaden`) instead of code (`region=84`), causing empty-query cascades and snapshot failures.

Durable guidance:

- Runtime should support both options query shapes:
  - 1 column: value=label.
  - 2 columns: col1=value, col2=label.
- Agent-facing docs (`/skills/dashboard/SKILL.md`) and framework spec must match runtime semantics.
- Existing user skill copies under `data/user/{id}/skills/` can drift from `user_workspace/skills/`; update both when changing dashboard guidance.
