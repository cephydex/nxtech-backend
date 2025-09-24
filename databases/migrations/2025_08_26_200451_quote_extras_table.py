"""QuoteExtrasTable Migration."""

from masoniteorm.migrations import Migration


class QuoteExtrasTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("quote_extras") as table:
            # table.uuid("id").primary()
            table.primary(["quote_id", "insurance_company_id"])
            table.uuid("quote_id")
            table.uuid("insurance_company_id")
            table.foreign("quote_id").references("id").on("quotes")
            # table.enum("type", ["deductible", "exclusion", "special_condition"]).default("deductible")
            # extra_data = {
            #     "deductibles": [{"Motor vehicle": "10%"}], "exclusions":"We are excluding all possible", 
            #     "special_condition": "No condition is permanent"
            # }            
            table.jsonb("extras").nullable()
            table.decimal("quote_amount", 10, 2)
            table.boolean("accepted").default(False)
            table.uuid("created_by")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("quote_extras")
