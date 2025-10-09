"""PoliciesTable Migration."""

from masoniteorm.migrations import Migration


class PoliciesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("policies") as table:
            table.uuid("id").primary()
            table.uuid("quote_id").unique()
            table.foreign("quote_id").references('id').on('quotes')
            table.date("start_date")
            table.date("expiry_date")
            table.uuid("created_by")
            table.uuid("policy_type_id")
            table.uuid("project_id").nullable()
            table.uuid("client_id").nullable()
            # table.foreign("project_id").references('id').on('projects')
            table.jsonb("quote_props").nullable()
            table.uuid("insurance_company_id")
            table.decimal("quote_amount", 10, 2)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("policies")
