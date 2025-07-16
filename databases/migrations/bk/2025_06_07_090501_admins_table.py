"""AdminsTable Migration."""

from masoniteorm.migrations import Migration


class AdminsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("admins") as table:
            table.uuid("id").primary()
            table.uuid("role_id")
            table.string("full_name")
            table.enum("sex", ['male', 'female']).default("male")
            table.string("phone_no", 20).unique()
            table.string("email").unique().nullable()
            table.string("password")
            table.string("inst")
            table.enum("active_status", ['active', "pending", 'blocked']).default("active")
            table.index("full_name", name="name_idx")
            table.foreign('role_id').references('id').on('roles')
            table.text('blocked_reason').nullable()

            table.timestamps()
            table.table_comment("Admins table")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("admins")
