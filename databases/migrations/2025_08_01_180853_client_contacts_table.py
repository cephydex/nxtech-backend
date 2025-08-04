"""ClientContactsTable Migration."""

from masoniteorm.migrations import Migration


class ClientContactsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("client_contacts") as table:
            table.uuid("id").primary()
            table.string("full_name")
            table.string("email").unique()
            table.string("contact_no")
            table.string("role").nullable()
            table.uuid("client_id")
            table.foreign("client_id").references('id').on('clients')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("client_contacts")
