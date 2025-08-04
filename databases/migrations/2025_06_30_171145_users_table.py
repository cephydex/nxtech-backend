"""UsersTable Migration."""

from masoniteorm.migrations import Migration


class UsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("users") as table:
            table.uuid("id").primary()
            table.string("email").unique()
            table.string("username").unique()
            table.string("password")
            table.enum("active_status", ['active', 'inactive', 'suspended']).default('active')
            # table.uuid("dept_id")
            # table.foreign("dept_id").references('id').on('departments')
            
            table.uuid("role_id")
            table.timestamp("last_login").nullable()
            table.text("remarks").nullable()
            table.foreign('role_id').references('id').on('user_roles')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("users")

# System Role Level (e.g., Admin, Read-Only, Edit, Approver)
# Access Permissions / Modules Assigned (e.g., Client Management, Policy, Finance, Commissions, Reports)
# User Status (Active / Inactive / Suspended)
# Date Added to System
# Last Login Date (for audit tracking)
# Supervisor or Reporting Line (optional – useful for workflow approvals)
# Remarks / Notes
