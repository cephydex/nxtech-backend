"""InsuranceCompaniesTable Migration."""

from masoniteorm.migrations import Migration


class InsuranceCompaniesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("insurance_companies") as table:
            table.uuid("id").primary()
            table.string("name").unique()
            table.string("postal_addr").nullable()
            table.string("contact_no").nullable()
            table.string("email").nullable()
            table.boolean("active_status").default(True)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("insurance_companies")
