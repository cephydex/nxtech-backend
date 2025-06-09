"""UsersTable Migration."""

from masoniteorm.migrations import Migration


class UsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("users") as table:
            table.uuid("id").primary()
            table.string("email").unique()
            table.string("username").unique()
            table.string("password")
            table.enum("active_status", ['pending', 'active', 'disabled']).default('active')
            
            table.uuid("role_id")
            table.foreign('role_id').references('id').on('user_roles')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("users")
