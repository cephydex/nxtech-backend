"""BizIntroducersTable Migration."""

from masoniteorm.migrations import Migration


class BizIntroducersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("biz_introducers") as table:
            table.uuid("id").primary()
            table.uuid("title_id")
            table.foreign('title_id').references('id').on('titles')
            table.string("full_name_introducer").nullable()
            table.string("primary_contact_name").nullable()
            table.string("email")
            table.string("contact_no")
            table.string("address").nullable()
            table.string("location").nullable()
            
            table.string("id_type").nullable()
            table.string("id_number").nullable()
            table.string("business_name").nullable()
            table.string("business_reg_no").nullable()
            table.string("tin_no").nullable()
            
            table.string("tin_no").nullable()
            table.string("bank_id").nullable()
            table.foreign('bank_id').references('id').on('banks')
            table.string("bank_account_name").nullable()
            table.string("bank_branch_name").nullable()
            table.string("bank_account_no").nullable()
            table.text("notes").nullable()
            
            table.decimal("commission_rate", 10, 2).nullable()
            table.uuid("user_id").nullable()
            table.foreign('user_id').references('id').on('users')
            table.unique(['first_name', 'last_name', 'contact_no'])
            table.enum("itype", ['Individual', 'Company']).default('Individual')
            table.enum("active_status", ['active', 'disabled']).default('active')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("biz_introducers")
        
# Full legal name of the business introducer or agent
# Type of Introducer (Individual / Company)
# Name of the primary contact for corporate introducers (If Corportae)
# Contact Number
# Email Address
# Address/Location
# ID Type
# ID Number
# Business Registration Number
# Tax Identification Number
# Bank Name
# Bank Account Name
# Bank Account Number
# Commission Rate (%)
# Status (Active / Inactive)
# Date Added to System
# Notes / Remarks
# Business Introducer Agreement Uploaded
