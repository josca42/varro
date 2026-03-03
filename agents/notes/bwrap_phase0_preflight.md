# Bubblewrap Phase 0 Preflight

Date: 2026-03-02.

- Added repeatable preflight script: `scripts/check_bwrap_phase0.sh`.
- Current `dev` result on Ubuntu 24.04 host:
  - `bubblewrap 0.9.0`
  - `kernel.unprivileged_userns_clone = 1`
  - `kernel.apparmor_restrict_unprivileged_userns = 1` initially
  - `unshare --user --map-root-user` works
  - `bwrap --unshare-user ...` fails with `setting up uid map: Permission denied`
- Impact:
  - `varro.agent.bash.run_bash_command(...)` in BWRAP mode fails on first command with the same uid map error.

Resolved on host by root:

- `sysctl -w kernel.apparmor_restrict_unprivileged_userns=0`
- `scripts/check_bwrap_phase0.sh` now returns `phase0_status=pass`
- `run_bash_command(...)` succeeds in BWRAP mode again.

For persistence across reboot (root):

- `printf 'kernel.apparmor_restrict_unprivileged_userns=0\n' > /etc/sysctl.d/60-varro-bwrap.conf`
- `sysctl --system`
- Host currently has only two definitions for this key:
  - `/usr/lib/sysctl.d/10-apparmor.conf` sets `1`
  - `/etc/sysctl.d/60-varro-bwrap.conf` sets `0` (override)

Prod execution note:

- `prod` cannot execute scripts under `/home/dev/...` unless it can traverse `/home/dev`.
- Run preflight from a neutral path:
  - `install -m 0755 /home/dev/varro/scripts/check_bwrap_phase0.sh /tmp/check_bwrap_phase0.sh`
  - `sudo -u prod /tmp/check_bwrap_phase0.sh`

Fallback only if policy cannot be changed:

- `dpkg-statoverride --quiet --remove /usr/bin/bwrap`
- `dpkg-statoverride --update --add root root 4755 /usr/bin/bwrap`
