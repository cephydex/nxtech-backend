"""ProductColumnsTable Migration."""

from masoniteorm.migrations import Migration


class ProductColumnsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("product_columns") as table:
            table.uuid("id").primary()
            table.jsonb("data")
            table.timestamps()


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("product_columns")

