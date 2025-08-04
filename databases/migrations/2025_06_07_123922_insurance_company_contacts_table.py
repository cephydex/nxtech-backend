"""InsuranceCompaniesTable Migration."""

from masoniteorm.migrations import Migration


class InsuranceCompanyContactsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("insurance_company_contacts") as table:
            table.uuid("id").primary()
            table.string("name").unique()
            table.string("contact_no").nullable()
            table.string("email").nullable()
            table.uuid("insurance_company_id")
            table.foreign("insurance_company_id").references("id").on("insurance_companies")
            table.string("role") # Claims, Underwriter
            table.boolean("is_active").default(True)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("insurance_company_contacts")
