"""ClientsTable Migration."""

from masoniteorm.migrations import Migration


class ClientsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("clients") as table:
            table.uuid("id").primary()
            table.string("client_code")
            table.enum("client_type", ["Individual", "Corporate"]).default("Corporate")
            table.string("company_name").unique().nullable()
            table.string("company_reg_no").unique().nullable()
            table.integer("year_of_inc").nullable()
            table.string("address_loc").nullable()
            table.string("email")
            table.string("contact_no")
            table.boolean("is_existing").default(False)
            table.string("uploaded_doc").nullable()
            table.string("tin_no").unique().nullable()
            table.enum("active_status", [
                    'active', 'inactive', 'dormant', 'terminated'
                ]).default('inactive')
            table.string("notes").nullable()
            table.uuid("account_manager").nullable() # also relationship officer
            table.foreign("account_manager").references('id').on('users')
            table.uuid("claims_manager").nullable() # also claims officer
            table.foreign("claims_manager").references('id').on('users')

            # individual part
            table.uuid("title_id").nullable()
            table.foreign('title_id').references('id').on('titles')
            table.string("first_name").nullable()
            table.string("last_name").nullable()
            table.string("other_names").nullable()

            table.date("dob").nullable()
            table.enum("sex", ["M", "F"]).default("F")
            table.uuid("nationality_id").nullable()
            table.foreign("nationality_id").references('id').on('nationalities')
            table.string("id_type").nullable()
            table.string("id_number").nullable()
            table.boolean("pep").default(False)
            table.string("employer_name").nullable()
            table.string("residential_addr").nullable()
            table.string("postal_addr").nullable()
            
            table.uuid("professional_group_id").nullable()
            table.foreign("professional_group_id").references('id').on('professional_groups')
            table.uuid("profession_id").nullable()
            table.foreign("profession_id").references('id').on('professions')
            # table.uuid("biz_intro_id").nullable()
            # table.foreign("biz_intro_id").references('id').on('biz_introducers')            
            table.uuid("created_by")
            table.foreign("created_by").references('id').on('users')
            table.uuid("login_id").nullable()
            table.foreign("login_id").references('id').on('users')
            table.timestamps()
            
    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("clients")

