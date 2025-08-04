"""PolicyTypesTable Migration."""

from masoniteorm.migrations import Migration


class PolicyTypesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("policy_types") as table:
            table.increments("id")
            table.uuid("cat_id")
            table.foreign("cat_id").references("id").on("policy_categories")
            table.string("name")
            table.text("description").nullable()
            table.decimal("commission", 10, 2).nullable()

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("policy_types")
