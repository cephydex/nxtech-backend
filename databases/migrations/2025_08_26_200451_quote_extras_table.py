"""QuoteExtrasTable Migration."""

from masoniteorm.migrations import Migration


class QuoteExtrasTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("quote_extras") as table:
            # id, quote_id, description, type, created_at, updated_at
            table.uuid("id").primary()
            table.uuid("quote_id")
            table.foreign("quote_id").references("id").on("quotes")
            table.enum("type", ["deductible", "exclusion", "special_condition"]).default("deductible")
            table.text("description")
            # table.primary("description")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("quote_extras")
