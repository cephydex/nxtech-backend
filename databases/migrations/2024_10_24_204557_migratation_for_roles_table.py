"""MigrtationForRolesTable Migration."""

from masoniteorm.migrations import Migration
import uuid


class MigratationForRolesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("user_roles") as table:
            # table.uuid("id").primary().default("uuid_generate_v4()")
            table.uuid("id").primary()
            table.string("name").unique()
            table.text("description").nullable()

            table.timestamps()
            table.table_comment("Roles table")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("user_roles")
