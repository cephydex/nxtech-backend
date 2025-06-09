"""ProfessionsTable Migration."""

from masoniteorm.migrations import Migration


class ProfessionsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("professions") as table:
            table.uuid("id").primary()
            table.string("code").nullable().unique()
            table.string("name").unique()
            
            table.uuid("group_id")
            table.foreign('group_id').references('id').on('professional_groups')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("professions")
