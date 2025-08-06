"""ProspectNotesTable Migration."""

from masoniteorm.migrations import Migration


class ProspectStagesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("prospect_stages") as table:
            table.uuid("prospect_id")
            table.foreign("prospect_id").references("id").on("prospects")
            table.string("stage")
            table.text("notes").nullable()
            table.timestamps()
            table.unique(["prospect_id", "stage"])

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("prospect_notes")
