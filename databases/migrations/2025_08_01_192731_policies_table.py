"""PoliciesTable Migration."""

from masoniteorm.migrations import Migration


class PoliciesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("policies") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("policies")
