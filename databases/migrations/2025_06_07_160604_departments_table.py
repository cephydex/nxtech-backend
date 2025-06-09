"""DepartmentsTable Migration."""

from masoniteorm.migrations import Migration


class DepartmentsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("departments") as table:
            table.uuid("id").primary()
            table.string("name").unique()
            table.string("code").unique().nullable()
            table.text("description").nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("departments")
