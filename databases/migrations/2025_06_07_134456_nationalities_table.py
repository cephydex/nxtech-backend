"""NationalitiesTable Migration."""

from masoniteorm.migrations import Migration


class NationalitiesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("nationalities") as table:
            table.uuid("id").primary()
            table.string("nationality")
            table.string("short_name")
            table.integer("num_code").nullable()
            table.string("alpha_2_code")
            table.string("alpha_3_code").nullable()
            table.unique(["nationality", 'short_name'])
                        
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("nationalities")
