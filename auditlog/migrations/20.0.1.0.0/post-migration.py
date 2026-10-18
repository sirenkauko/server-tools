# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


def migrate(cr, version):
    """Rename rule state 'subscribed' to 'confirmed'.

    This rename was introduced by the 19.0.1.0.0 migration script, which is not
    run when a database jumps from an older version straight to 20.0.
    Idempotent: it is a no-op once the rename has been applied.
    """
    cr.execute(
        "update auditlog_rule set state = 'confirmed' where state = 'subscribed';"
    )
