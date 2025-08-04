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
            table.enum("company_type", ["Life", "Non-Life", "Health"]).default("Non-Life")
            table.string("head_office_addr").nullable()
            table.string("contact_no").nullable()
            table.string("md_name").nullable()
            table.string("md_email").nullable()
            table.string("nic_license_no").nullable()
            table.string("biz_reg_no").nullable()
            table.string("tin_no").nullable()
            table.enum("partnership_type", ["Delegated Authority", "Just Broking"]).nullable()
            table.string("bank_id").nullable()
            table.string("bank_account_name").nullable()
            table.string("bank_account_no").nullable()

            table.boolean("active_status").default(True)
            table.text("notes").nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("insurance_companies")
