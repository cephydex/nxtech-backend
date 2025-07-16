"""TitlesTable Migration."""

from masoniteorm.migrations import Migration


class TitlesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("titles") as table:
            table.uuid("id").primary()
            table.string("name").unique()
            table.timestamps()
            table.table_comment("Titles table")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("titles")
