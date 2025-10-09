"""QuotesTable Migration."""

from masoniteorm.migrations import Migration


class QuotesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("quotes") as table:
            table.uuid("id").primary()
            table.uuid("prospect_id").nullable()
            table.uuid("project_id")
            table.foreign("project_id").references("id").on("projects")
            table.uuid("created_by")
            table.uuid("policy_type_id")
            table.uuid("insurance_company_id").nullable()
            table.decimal("premium", 10, 2)
            table.string("currency").nullable().default('GHS')
            table.date("valid_until").nullable()
            table.string("status")
            table.string("document_url").nullable()
            table.jsonb("entry_data")
            table.bool("has_policy").default(False)
            table.timestamps()
            # id, lead_id, product_code, coverage, premium, currency, valid_until, status, quote_document_url

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("quotes")
