"""BizIntroducersTable Migration."""

from masoniteorm.migrations import Migration


class BizIntroducersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("biz_introducers") as table:
            table.uuid("id").primary()
            table.uuid("title_id")
            table.foreign('title_id').references('id').on('titles')
            table.string("first_name")
            table.string("last_name")
            table.string("email")
            table.string("mobile_no")
            table.string("address").nullable()
            table.string("company_name").nullable()
            table.string("location").nullable()
            table.decimal("share_percentage", 10, 2).nullable()
            table.uuid("user_id").nullable()
            table.foreign('user_id').references('id').on('users')
            table.unique(['first_name', 'last_name', 'mobile_no'])

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("biz_introducers")
