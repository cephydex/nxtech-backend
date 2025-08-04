"""ProfessionalGroupsTable Migration."""

from masoniteorm.migrations import Migration


class ProfessionalGroupsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("professional_groups") as table:
            table.uuid("id").primary()
            table.string("name").unique()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("professional_groups")
