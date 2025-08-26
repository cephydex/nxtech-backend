"""ProspectNotesTable Migration."""

from masoniteorm.migrations import Migration


class ProjectStagesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("project_stages") as table:
            # table.uuid("prospect_id")
            # table.foreign("prospect_id").references("id").on("prospects")
            table.uuid("created_by")
            table.uuid("project_id")
            table.foreign("project_id").references("id").on("projects")
            table.string("stage")
            table.text("notes").nullable()
            table.timestamps()
            table.unique(["project_id", "stage"])

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("project_stages")

# stages
# 1. Initial Contact, 2. Receipt of Document or Insurance Details, 3. Quotation Sent, 4. Client Reviewing
# 5. Negotiation, 6. Awaiting Decision, 7. Closed – Won, 7. Closed – Lost

