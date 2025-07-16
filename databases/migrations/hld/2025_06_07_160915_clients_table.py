"""ClientsTable Migration."""

from masoniteorm.migrations import Migration


class ClientsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("clients") as table:
            table.uuid("id").primary()
            table.string("account_no").unique().nullable()
            table.string("national_id").unique().nullable()
            table.uuid("title_id")
            table.foreign('title_id').references('id').on('titles')
            table.string("first_name")
            table.string("last_name")
            table.string("other_names").nullable()
            table.string("email")
            table.string("address")
            table.string("address2").nullable()
            table.string("mobile_no")
            table.string("mobile_no2").nullable()
            table.string("tel_no").nullable()
            table.date("dob")
            table.string("company_name").nullable()
            table.enum("active_status", [
                    'active', 'unapproved', 'disabled', 'suspended'
                ]).default('unapproved')
            table.enum("marital_status", [
                    'married', 'remarried', 'single', 'widowed', 'separated', 'divorced', 'engaged'
                ]).default("single")
            table.string("driver_license_no").nullable()
            table.string("driver_license_cat").nullable()
            
            table.uuid("professional_group_id").nullable()
            table.foreign("professional_group_id").references('id').on('professional_groups')
            table.uuid("profession_id").nullable()
            table.foreign("profession_id").references('id').on('professions')
            table.uuid("biz_intro_id").nullable()
            table.foreign("biz_intro_id").references('id').on('biz_introducers')
            table.uuid("nationality_id")
            table.foreign("nationality_id").references('id').on('nationalities')
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
