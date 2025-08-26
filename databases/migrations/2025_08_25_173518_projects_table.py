"""ProjectsTable Migration."""

from masoniteorm.migrations import Migration


class ProjectsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("projects") as table:
            table.uuid("id").primary()
            table.uuid("prospect_id")
            table.foreign("prospect_id").references("id").on("prospects")
            table.uuid("created_by")
            table.foreign("created_by").references('id').on('users')
            table.string("status")
            table.uuid("policy_type_id").nullable()
            # table.uuid("prospect_id")
            # table.unique("prospect_id", "policy_type_id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("projects")
