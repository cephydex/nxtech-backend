"""UsersTableAlter Migration."""

from masoniteorm.migrations import Migration


class UsersTableAlter(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("users") as table:
            table.string("first_name").nullable()
            table.string("last_name").nullable()
            table.string("initials").nullable()
            table.uuid("dept_id").nullable()
            table.foreign("dept_id").references("id").on("departments")
            # table.uuid("role_id").nullable()
            # table.foreign("role_id").references("id").on("roles")
            table.uuid("supervisor_id").nullable()
            # table.foreign("role_id").references("id").on("roles")
            pass

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("users") as table:
            pass

# Full Name (First Name + Last Name) 
# User Initials
# User Role / Designation (Admin, Account Manager, Finance Officer, Claims Officer, Management)
# Department / Unit (Technical, Claims, Finance, Admin, Sales)
# System Role Level (e.g., Admin, Read-Only, Edit, Approver)
# Access Permissions / Modules Assigned (e.g., Client Management, Policy, Finance, Commissions, Reports)
# User Status (Active / Inactive / Suspended)
# Date Added to System
# Last Login Date (for audit tracking)
# Supervisor or Reporting Line (optional – useful for workflow approvals)
# Remarks / Notes

