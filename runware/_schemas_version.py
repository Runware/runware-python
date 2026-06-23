"""
Pinned schemas bundle version used by the type generator.

Managed by ``scripts/bump_schemas.sh`` — run that to advance to the current
latest release. Don't edit by hand except when intentionally rolling back to
an older pin (historical reference, hotfix branch, debugging a regression).

Read at build time only — runtime schema validation hits the live
``/resolve/<model>`` endpoint and doesn't consult this constant.
"""

SCHEMAS_VERSION = "20260623105208"
