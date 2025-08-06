"""PropectsTable Migration."""

from masoniteorm.migrations import Migration


class ProspectsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("prospects") as table:
            table.uuid("id").primary()
            table.enum("client_type", ["Individual", "Corporate"]).default("Corporate")
            table.string("company_name").unique().nullable()
            table.integer("year_of_inc").nullable()
            table.string("address_loc").nullable()
            table.string("email")
            table.string("contact_no")

            table.uuid("title_id").nullable()
            table.foreign('title_id').references('id').on('titles')
            table.string("first_name").nullable()
            table.string("last_name").nullable()
            table.string("other_names").nullable()
            table.enum("sex", ["M", "F"]).default("F")
            table.uuid("nationality_id").nullable()

            # table.string("stage")
            table.string("source")
            table.uuid("created_by")
            table.foreign("created_by").references('id').on('users')
            table.enum("active_status", [
                    'active', 'inactive', 'dormant', 'terminated'
                ]).default('inactive')
            # table.text("notes").nullable()
            table.timestamps()
            table.unique(["email", "contact_no"])
            
    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("prospects")
