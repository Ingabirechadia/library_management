# Copyright (c) 2026, Chadia and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LibrarySettings(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		fine_per_day: DF.Int
		loan_period_days: DF.Int
		max_books_per_member: DF.Int
	# end: auto-generated types

	_DOCTYPE_NAME = "Library Settings"
