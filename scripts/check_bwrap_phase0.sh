#!/usr/bin/env bash
set -euo pipefail

bwrap_probe_cmd=(
  bwrap
  --unshare-user
  --uid 0
  --gid 0
  --ro-bind /
  /
  --proc /proc
  --dev /dev
  /bin/sh
  -lc
  'echo ok; id -u; cat /proc/self/uid_map; cat /proc/self/gid_map'
)

echo "== identity =="
id
echo

echo "== bubblewrap =="
if ! command -v bwrap >/dev/null 2>&1; then
  echo "bwrap not found in PATH"
  exit 1
fi
bwrap --version
echo

echo "== kernel settings =="
for key in user.max_user_namespaces kernel.unprivileged_userns_clone kernel.apparmor_restrict_unprivileged_userns; do
  if sysctl "$key" >/dev/null 2>&1; then
    sysctl "$key"
  else
    echo "$key = <not available>"
  fi
done
echo

echo "== unshare baseline =="
if unshare --user --map-root-user /bin/sh -lc 'id -u >/dev/null'; then
  echo "unshare user namespace: ok"
else
  echo "unshare user namespace: failed"
fi
echo

echo "== bwrap fail-closed probe =="
set +e
probe_output="$("${bwrap_probe_cmd[@]}" 2>&1)"
probe_rc=$?
set -e
printf '%s\n' "$probe_output"
echo

if [ "$probe_rc" -eq 0 ]; then
  echo "phase0_status=pass"
  exit 0
fi

echo "phase0_status=fail"
if [[ "$probe_output" == *"setting up uid map: Permission denied"* ]]; then
  echo "phase0_reason=uid_map_permission_denied"
fi
exit 1
