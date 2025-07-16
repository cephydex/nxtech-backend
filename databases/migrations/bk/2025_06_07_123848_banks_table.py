"""BanksTable Migration."""

from masoniteorm.migrations import Migration


class BanksTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("banks") as table:
            table.uuid("id").primary()
            table.string("name").unique()
            table.string("code").nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("banks")
