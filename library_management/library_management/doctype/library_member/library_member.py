# Copyright (c) 2026, Chadia and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LibraryMember(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		email: DF.Text | None
		joined_on: DF.Date | None
		member_name: DF.Data
		membership_type: DF.Literal["student", "staff", "public"]
		naming_series: DF.Data | None
		phone: DF.Phone | None
		status: DF.Literal["active", "suspended"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Library Member"
