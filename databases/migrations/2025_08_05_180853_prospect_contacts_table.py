"""ClientContactsTable Migration."""

from masoniteorm.migrations import Migration


class ProspectContactsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("prospect_contacts") as table:
            table.uuid("id").primary()
            table.string("full_name")
            table.string("email").unique()
            table.string("contact_no")
            table.string("role").nullable()
            table.uuid("prospect_id")
            table.foreign("prospect_id").references('id').on('prospects')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("prospect_contacts")
