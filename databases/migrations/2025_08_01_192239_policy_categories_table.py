"""PolicyCategoriesTable Migration."""

from masoniteorm.migrations import Migration


class PolicyCategoriesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("policy_categories") as table:
            table.uuid("id").primary()
            table.string("name").unique()
            table.text("description").nullable()

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("policy_categories")
