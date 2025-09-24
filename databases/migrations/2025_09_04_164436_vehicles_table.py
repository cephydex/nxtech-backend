"""VehiclesTable Migration."""

from masoniteorm.migrations import Migration


class VehiclesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("vehicles") as table:
            table.uuid("id")
            table.string("brand")
            table.jsonb("models")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("vehicles")
