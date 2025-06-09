"""MigrationForAdminsTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForAdminsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("admins") as table:
            table.uuid("id").primary()
            table.uuid("role_id")
            table.string("first_name")
            table.string("last_name")
            table.string("other_names").nullable()
            table.enum("sex", ['male', 'female']).default("male")
            table.string("phone", 20).unique()
            table.string("email").unique().nullable()
            table.string("password")
            table.string("inst")
            table.enum("active_status", ['active', "pending", 'blocked']).default("active")
            table.index(["first_name", "last_name", "other_names"], name="name_idx")
            table.foreign('role_id').references('id').on('roles')
            table.text('blocked_reason').nullable()
            # table.primary(['id', 'email'])
            # table.unique(['email', 'phone_number'])

            table.timestamps()
            table.table_comment("Admins table")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("admins")
