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
            table.string("email")
            table.string("address1")
            table.string("address2").nullable()
            table.string("mobile_no")
            table.string("tel_no")
            table.date("dob")
            table.enum("active_status", [
                    'active', 'unapproved', 'disabled', 'suspended'
                ]).default('unapproved')
            table.enum("marital_status", [
                    'married', 'remarried', 'single', 'widowed', 'separated', 'divorced', 'engaged'
                ]).default("single")
            table.string("driver_license_no").nullable()
            table.string("driver_license_cat").nullable()
            
            table.uuid("profession_id")
            table.foreign("profession_id").references('professions').on('id')
            table.uuid("nationality_id")
            table.foreign("nationality_id").references('nationalities').on('id')
            table.uuid("created_by")
            table.foreign("created_by").references('users').on('id')
            table.uuid("login_id").nullable()
            table.foreign("login_id").references('users').on('id')

            table.timestamps()

            # id, Title, name, long_name, address1, address2, mail_address
            # dob, status, professional_group, profession, nationality, mobile_no, tel_no
            # driver_license_no, driver_license_cat, email, account_no
            
    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("clients")
