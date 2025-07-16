"""AgentsTable Migration."""

from masoniteorm.migrations import Migration


class AgentsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("agents") as table:
            table.uuid("id").primary()
            table.uuid("title_id")
            table.foreign('title_id').references('id').on('titles')
            table.string("first_name")
            table.string("last_name")
            table.string("initials").nullable()
            table.string("email")
            table.string("mobile_no")
            table.string("address")
            table.foreign('dept_id').references('id').on('departments')
            # table.string("company_name").nullable()
            table.uuid("user_id").nullable()
            table.uuid("reports_to").nullable()
            table.foreign('user_id').references('id').on('users')
            table.foreign('reports_to').references('id').on('agents')
            table.unique(['first_name', 'last_name', 'mobile_no'])

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("agents")

        
        
# Full Name (First Name + Last Name) 
# User Initials
# User Role / Designation (Admin, Account Manager, Finance Officer, Claims Officer, Management)
# Department / Unit (Technical, Claims, Finance, Admin, Sales)

