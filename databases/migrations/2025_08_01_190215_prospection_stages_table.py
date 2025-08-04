"""ProspectionStagesTable Migration."""

from masoniteorm.migrations import Migration


class ProspectionStagesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("prospection_stages") as table:
            table.uuid("user_id")
            table.foreign("user_id").references('id').on('users')
            table.uuid("client_id")
            table.enum("source", [
                    "Referral", "Cold Call", "Website Inquiry", "Walk-in", "Global Introduction"
                ]).default("Referral")
            table.string("stage")
            table.string("entry_date")
            table.text("notes").nullable()
            table.timestamps()
            
            table.primary(["client_id", "stage"])

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("prospection_stages")

# Initial Contact, Receipt of Document or Insurance Details, Quotation Sent, Client Reviewing, 
# Negotiation, Awaiting Decision, Closed – Won, Closed – Lost
# Initial Contact (indicate date)
# Receipt of Document or Insurance Details (indicate date)
# Quotation Sent (indicate date)
# Client Reviewing (indicate date)
# Negotiation (indicate date)
# Awaiting Decision (indicate date)
# Closed – Won (indicate date)
# Closed – Lost (indicate date)

